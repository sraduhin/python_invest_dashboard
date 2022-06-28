from tinkoff.invest import Client
from flask import current_app
from webapp.portfolio.save_assets import save_assets


def get_assets():
    """ Функция извлекает из API данные биржевых инструментов
    и сохраняет в таблицу по типу бумаги"""
    TOKEN = current_app.config['TINKOFF_API_KEY']
    save_assets_by_type(TOKEN, 'shares')
    save_assets_by_type(TOKEN, 'bonds')
    save_assets_by_type(TOKEN, 'etfs')
    save_assets_by_type(TOKEN, 'currencies')
    save_assets_by_type(TOKEN, 'futures')


def save_assets_by_type(token, type):
    with Client(token) as client:
        if hasattr(client.instruments, type):
            instrument_class = getattr(client.instruments, type)
            instruments = instrument_class().instruments
            for instrument in instruments:
                figi = instrument.figi
                tiker = instrument.ticker
                name = instrument.name
                currency = instrument.currency
                save_assets(figi, tiker, type, name, currency)


if __name__ == '__main__':
    print(get_assets())