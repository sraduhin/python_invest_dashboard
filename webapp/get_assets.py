from time import sleep
from tinkoff.invest import Client
from flask import current_app
from webapp.save_assets import save_assets

def get_assets():
    TOKEN = current_app.config['TINKOFF_API_KEY']
    with Client(TOKEN) as client:
        instruments = client.instruments.get_assets().assets
        for instrument in instruments:
            instrument_dict = instrument.instruments[0]
            name = instrument.name
            figi = instrument_dict.figi
            type = instrument_dict.instrument_type
            tiker = instrument_dict.ticker
            class_code = instrument_dict.class_code
            save_assets(name, figi, type, tiker, class_code)
                
if __name__ == '__main__':
    print(get_assets())