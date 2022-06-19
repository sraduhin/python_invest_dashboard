from sqlalchemy import null
from tinkoff.invest import Client
from flask import current_app
from webapp.save_portfolios import save_portfolios
from webapp.normalize import normalize_floatings

def get_portfolios():
    TOKEN = current_app.config['TINKOFF_API_KEY']
    with Client(TOKEN) as client:
        accounts = client.users.get_accounts().accounts # Приводим к виду [Account(...), Account(...), ...]

        for account in accounts:
            account_id = account.id
            type = account.type
            if account.access_level in [1, 2]:
                data = True
                portfolio = client.operations.get_portfolio(account_id=account_id)
                expected_yield = normalize_floatings(portfolio.expected_yield)
                total_currencies = normalize_floatings(portfolio.total_amount_currencies)
                total_shares = normalize_floatings(portfolio.total_amount_shares)
                total_etf = normalize_floatings(portfolio.total_amount_etf)
                total_bonds = normalize_floatings(portfolio.total_amount_bonds)
                total_futures = normalize_floatings(portfolio.total_amount_futures)
                save_portfolios(account_id, type, data, expected_yield, total_currencies, total_shares, total_etf, total_bonds, total_futures)
            else:
                data = False
                save_portfolios(account_id, type, data, expected_yield=None, total_currencies=None, total_shares=None, total_etf=None, total_bonds=None, total_futures=None)
                
if __name__ == '__main__':
    print(get_portfolios())
    