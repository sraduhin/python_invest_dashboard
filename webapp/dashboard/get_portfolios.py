from tinkoff.invest import Client
from flask_login import current_user
from webapp.dashboard.save_portfolios import save_portfolios
from webapp.dashboard.normalize import normalize_floatings


def get_portfolios():
    """ Функция извлекает из API данные для аккаунтов с уровнем доступа
    1: full-access и 2: read-only"""
    TOKEN = current_user.api_key
    user_id = current_user.id
    with Client(TOKEN) as client:
        accounts = client.users.get_accounts().accounts
        for account in accounts:
            type = account.type
            account_id = account.id
            if account.access_level in [1, 2]:
                portfolio = client.operations.get_portfolio(account_id=account_id)
                expected_yield = normalize_floatings(portfolio.expected_yield)
                total_shares = normalize_floatings(portfolio.total_amount_shares)
                total_bonds = normalize_floatings(portfolio.total_amount_bonds)
                total_etf = normalize_floatings(portfolio.total_amount_etf)
                total_currencies = normalize_floatings(portfolio.total_amount_currencies)
                total_futures = normalize_floatings(portfolio.total_amount_futures)
                save_portfolios(user_id, account_id, expected_yield, total_shares,
                                total_bonds, total_etf, total_currencies, total_futures, type)


if __name__ == '__main__':
    print(get_portfolios())
