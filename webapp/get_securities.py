from tinkoff.invest import Client
from flask import current_app
from webapp.save_securities import save_securities

def get_portfolio():
    TOKEN = current_app.config['TINKOFF_API_KEY']
    with Client(TOKEN) as client:
        accounts = client.users.get_accounts().accounts # Приводим к виду [Account(...), Account(...), ...]
    
        accounts = [account.id for account in accounts if account.access_level in [1,2]]
        for account in accounts:
            portfolio = client.operations.get_portfolio(account_id=account)
            portfolio = portfolio.positions
            for position in portfolio:
                figi = position.figi
                instrument_type = position.instrument_type
                currency = position.current_price.currency
                quantity = position.quantity.units + position.quantity.nano / 1000000000
                expected_yield = position.expected_yield.units + position.expected_yield.nano / 1000000000
                average_position_price_pt = position.average_position_price_pt.units + position.average_position_price_pt.nano / 1000000000
                quantity_lots = position.quantity_lots.units + position.quantity_lots.nano / 1000000000
                average_position_price = position.average_position_price.units + position.average_position_price.nano / 1000000000
                current_nkd = position.current_nkd.units + position.current_nkd.nano / 1000000000
                current_price = position.current_price.units + position.current_price.nano / 1000000000
                average_position_price_fifo = position.average_position_price_fifo.units + position.average_position_price_fifo.nano / 1000000000
                save_securities(figi, instrument_type, currency, quantity, average_position_price,
                                expected_yield, current_nkd, average_position_price_pt, current_price,
                                average_position_price_fifo, quantity_lots)
                
if __name__ == '__main__':
    print(get_portfolio())