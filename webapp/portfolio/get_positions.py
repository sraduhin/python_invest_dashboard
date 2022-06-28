from tinkoff.invest import Client
from flask import current_app
from webapp.portfolio.save_positions import save_positions
from webapp.portfolio.normalize import normalize_floatings
from webapp.portfolio.models import Portfolio, Instrument

def get_positions():
    """Функция извлекает из API данные для аккаунтов с уровнем доступа:
    1: full access; 2: read-only"""
    TOKEN = current_app.config['TINKOFF_API_KEY']
    with Client(TOKEN) as client:
        portfolios = Portfolio.query.all()
        for portfolio in portfolios:
            positions = client.operations.get_portfolio(account_id=portfolio.account_id).positions
            portfolio_id = portfolio.id
            for position in positions:
                figi = position.figi
                instrument = Instrument.query.filter(Instrument.figi == figi).first()
                instrument_id = instrument.id
                amount = normalize_floatings(position.quantity)
                expected_yield = normalize_floatings(position.expected_yield)
                average_price = normalize_floatings(position.average_position_price)
                current_price = normalize_floatings(position.current_price)
                lots = normalize_floatings(position.quantity_lots)
                save_positions(portfolio_id, instrument_id, amount, expected_yield,
                                average_price, current_price, lots)


if __name__ == '__main__':
    print(get_positions())

