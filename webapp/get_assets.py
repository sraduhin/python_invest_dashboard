from tinkoff.invest import Client
#from flask import current_app
from webapp.save_assets import save_assets
from webapp.config import TINKOFF_API_KEY



def get_assets():
    #TOKEN = current_app.config['TINKOFF_API_KEY']
    TOKEN = TINKOFF_API_KEY
    with Client(TOKEN) as client:
        save_assets_by_type(client, 'shares')


def save_assets_by_type(client, type):
    if not hasattr(client.instruments, type):
        instruments = getattr(client.instruments, type).instruments
        for instrument in instruments:
            figi = instrument.figi
            tiker = instrument.ticker
            name = instrument.name
            currency = instrument.currency
            return (figi, tiker, name)
        save_assets(figi, tiker, type, name, currency)


if __name__ == '__main__':
    print(get_assets())