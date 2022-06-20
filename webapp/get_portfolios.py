from os import access
from sqlalchemy import null
from tinkoff.invest import Client
from flask import current_app
from webapp.save_portfolios import save_portfolios
from webapp.normalize import normalize_floatings

def get_portfolios():
    """ Функция возвращает данные для аккаунтов с уровнем доступа
    1: full-access и 2: read-only"""
    TOKEN = current_app.config['TINKOFF_API_KEY']
    with Client(TOKEN) as client:
        accounts = client.users.get_accounts().accounts

        for account in accounts:
            type = account.type
            access_level = account.access_level
            account = account.id
            if access_level in [1, 2]:
                portfolio = client.operations.get_portfolio(account_id=account)
                expected_yield = normalize_floatings(portfolio.expected_yield)
                total_shares = normalize_floatings(portfolio.total_amount_shares)
                total_bonds = normalize_floatings(portfolio.total_amount_bonds)
                total_etf = normalize_floatings(portfolio.total_amount_etf)
                total_currencies = normalize_floatings(portfolio.total_amount_currencies)
                total_futures = normalize_floatings(portfolio.total_amount_futures)
                save_portfolios(account, type, expected_yield,total_shares,
                                total_bonds, total_etf, total_currencies, total_futures)
                
if __name__ == '__main__':
    print(get_portfolios())
