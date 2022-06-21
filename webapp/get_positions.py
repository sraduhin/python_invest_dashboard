from tinkoff.invest import Client
from flask import current_app
from webapp.save_positions import save_positions
from webapp.normalize import normalize_floatings
from webapp.model import Portfolio, Instrument

def get_positions():
    TOKEN = current_app.config['TINKOFF_API_KEY']
    with Client(TOKEN) as client:
        accounts = client.users.get_accounts().accounts
        accounts = [account.id for account in accounts if account.access_level in [1, 2]]
        for account in accounts:
            positions = client.operations.get_portfolio(account_id=account).positions
            portfolio = Portfolio.query.filter(Portfolio.account_id == account).first()
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

