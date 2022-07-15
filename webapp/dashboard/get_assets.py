from tinkoff.invest import Client
from flask import current_app
from webapp.dashboard.models import Instrument
from webapp.dashboard.save_assets import save_assets


def get_assets():
    """ Функция извлекает из API данные биржевых инструментов
    и сохраняет в таблицу по типу бумаги"""
    query = Instrument.query.first()
    if not query:
        print(' **!** Loading instrument list')
        TOKEN = current_app.config['TINKOFF_API_KEY']
        save_assets_by_type(TOKEN, 'shares')
        print(' **!** 25%')
        save_assets_by_type(TOKEN, 'bonds')
        print(' **!** 50%')
        save_assets_by_type(TOKEN, 'etfs')
        print(' **!** 75%')
        save_assets_by_type(TOKEN, 'currencies')
        print(' **!** 100%')
        save_assets_by_type(TOKEN, 'futures')
        print(' **!** Success')


def save_assets_by_type(token, type, sector=None):
    with Client(token) as client:
        if hasattr(client.instruments, type):
            instrument_class = getattr(client.instruments, type)
            instruments = instrument_class().instruments
            for instrument in instruments:
                if type == 'shares':
                    sector = instrument.sector
                figi = instrument.figi
                tiker = instrument.ticker
                name = instrument.name
                currency = instrument.currency
                save_assets(figi, tiker, type, name, currency, sector)


if __name__ == '__main__':
    print(get_assets())