from tinkoff.invest import Client
from flask import current_app
from webapp.save_shares import save_shares

def get_shares():
    TOKEN = current_app.config['TINKOFF_API_KEY']
    with Client(TOKEN) as client:
        INSTRUMENT_STATUS = 1 # 1: Instruments available for trading through Tinkoff API 2: All instruments
        shares = client.instruments.shares(instrument_status=INSTRUMENT_STATUS)
        shares = shares.instruments
        for share in shares:
            name = share.name
            figi = share.figi
            tiker = share.ticker
            classCode = share.class_code
            exchange = share.exchange
            currency = share.currency
            save_shares(name, figi, tiker, classCode, exchange, currency)
                
if __name__ == '__main__':
    print(get_shares())
