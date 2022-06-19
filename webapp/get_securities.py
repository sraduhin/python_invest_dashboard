from time import sleep
from tinkoff.invest import Client
from flask import current_app
from webapp.save_securities import save_securities
from webapp.normalize import normalize_floatings

def get_securities():
    TOKEN = current_app.config['TINKOFF_API_KEY']
    with Client(TOKEN) as client:
        accounts = client.users.get_accounts().accounts # Приводим к виду [Account(...), Account(...), ...]
    
        accounts = [account.id for account in accounts if account.access_level in [1,2]]
        INSTRUMENT_ID_TYPE_FIGI = 1 # type = figi
        for account in accounts:
            portfolio = client.operations.get_portfolio(account_id=account)
            portfolio = portfolio.positions
            assets = client.instruments
            for position in portfolio:
                account_id = account
                figi = position.figi
                currency = position.current_price.currency
                print(figi)
                name = assets.get_instrument_by(id_type=INSTRUMENT_ID_TYPE_FIGI, class_code="", id=figi).instrument.name
                tiker = assets.get_instrument_by(id_type=INSTRUMENT_ID_TYPE_FIGI, class_code="", id=figi).instrument.ticker
                class_code = assets.get_instrument_by(id_type=INSTRUMENT_ID_TYPE_FIGI, class_code="", id=figi).instrument.class_code
                exchange = assets.get_instrument_by(id_type=INSTRUMENT_ID_TYPE_FIGI, class_code="", id=figi).instrument.exchange
                currency = assets.get_instrument_by(id_type=INSTRUMENT_ID_TYPE_FIGI, class_code="", id=figi).instrument.currency
                amount = normalize_floatings(position.quantity)
                expected_yield = normalize_floatings(position.expected_yield)
                lots = normalize_floatings(position.quantity_lots)
                average_price = normalize_floatings(position.average_position_price)
                current_nkd = normalize_floatings(position.current_nkd)
                current_price = normalize_floatings(position.current_price)
                fifo = normalize_floatings(position.average_position_price_fifo)
                save_securities(account_id, figi, currency, name, tiker, class_code, exchange, amount, average_price,
                                expected_yield, current_nkd, current_price,
                                fifo, lots)
                sleep(1.6)
                
if __name__ == '__main__':
    print(get_securities())
    