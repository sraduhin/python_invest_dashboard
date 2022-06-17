from sqlalchemy import null
from tinkoff.invest import Client
from flask import current_app
from webapp.save_portfolios import save_portfolios

def get_portfolios():
    TOKEN = current_app.config['TINKOFF_API_KEY']
    with Client(TOKEN) as client:
        accounts = client.users.get_accounts().accounts # Приводим к виду [Account(...), Account(...), ...]

        for account in accounts:
            account_id = account.id
            type = account.type
            if account.access_level in [1, 2]:
                data = True
                divisor = 1000000000 # (units=5, nano=300000000) => units + nano / divisor = 5.30
                portfolio = client.operations.get_portfolio(account_id=account_id)
                expected_yield = portfolio.expected_yield.units + portfolio.expected_yield.nano / divisor
                total_currencies = portfolio.total_amount_currencies.units + portfolio.total_amount_currencies.nano / divisor
                total_shares = portfolio.total_amount_shares.units + portfolio.total_amount_shares.nano / divisor
                total_etf = portfolio.total_amount_etf.units + portfolio.total_amount_etf.nano / divisor
                total_bonds = portfolio.total_amount_bonds.units + portfolio.total_amount_bonds.nano / divisor
                total_futures = portfolio.total_amount_futures.units + portfolio.total_amount_futures.nano / divisor
                save_portfolios(account_id, type, data, expected_yield, total_currencies, total_shares, total_etf, total_bonds, total_futures)
            else:
                data = False
                save_portfolios(account_id, type, data, expected_yield=None, total_currencies=None, total_shares=None, total_etf=None, total_bonds=None, total_futures=None)
                
if __name__ == '__main__':
    print(get_portfolios())
    