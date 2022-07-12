from tinkoff.invest import Client
from flask import current_app
from webapp.dashboard.normalize import normalize_floatings
from webapp.dashboard.models import db
from webapp.dashboard.models import Portfolio, Instrument, Position

def get_positions():
    """Функция извлекает из API данные для аккаунтов с уровнем доступа:
    1: full access; 2: read-only"""
    TOKEN = current_app.config['TINKOFF_API_KEY']
    with Client(TOKEN) as client:
        portfolios = Portfolio.query.all()
        print(portfolios)
        for portfolio in portfolios:
            positions_API = client.operations.get_portfolio(account_id=portfolio.account_id).positions
            portfolio_id = portfolio.id
            position_API_list = [position.figi for position in positions_API]
            positions_db = Position.query.filter(Position.portfolio_id == portfolio_id).all()
            for position_db in positions_db:
                if position_db.figi not in position_API_list:
                    delete_position(position_db)
            position_db_list = [position.figi for position in positions_db]
            duplicate_figies = []
            for position_API in positions_API:
                if position_API.figi not in duplicate_figies:
                    duplicate_figies.append(position_API.figi)
                    if position_API.figi not in position_db_list:
                        add_position(position_API, portfolio_id)
                    else:
                        update_position(position_API)
                else:
                    sum_position(position_API)


def delete_position(position):
    db.session.delete(position)
    db.session.commit()


def add_position(position, portfolio_id):
    figi = position.figi
    print('save', figi)
    instrument = Instrument.query.filter(Instrument.figi == figi).first()
    instrument_id = instrument.id
    amount = normalize_floatings(position.quantity)
    expected_yield = normalize_floatings(position.expected_yield)
    average_price = normalize_floatings(position.average_position_price)
    current_price = normalize_floatings(position.current_price)
    position = Position(figi=figi, portfolio_id=portfolio_id, instrument_id=instrument_id,
                        amount=amount, expected_yield=expected_yield,
                        average_price=average_price, current_price=current_price)
    db.session.add(position)
    db.session.commit()


def update_position(position):
    print('update', position.figi)
    position_db = Position.query.filter(Position.figi == position.figi).first()
    position_db.amount = normalize_floatings(position.quantity)
    position_db.expected_yield = normalize_floatings(position.expected_yield)
    position_db.average_price = normalize_floatings(position.average_position_price)
    position_db.current_price = normalize_floatings(position.current_price)
    db.session.commit()


def sum_position(position):
    print('plus', position.figi)
    position_db = Position.query.filter(Position.figi == position.figi).first()
    position_db.amount += normalize_floatings(position.quantity)
    position_db.expected_yield += normalize_floatings(position.expected_yield)
    position_db.average_price += normalize_floatings(position.average_position_price)
    position_db.current_price += normalize_floatings(position.current_price)
    db.session.commit()


if __name__ == '__main__':
    print(get_positions())
