from webapp.dashboard.models import db, Portfolio


def save_portfolios(user_id, account_id, expected_yield, total_shares,
                    total_bonds, total_etf, total_currencies, total_futures, type):
    account_exists = Portfolio.query.filter(Portfolio.account_id == account_id).first()
    if not account_exists:
        portfolios = Portfolio(user_id=user_id, account_id=account_id, expected_yield=expected_yield, total_shares=total_shares,
                                total_bonds=total_bonds, total_etf=total_etf,
                                total_currencies=total_currencies,
                                total_futures=total_futures, type=type)
        db.session.add(portfolios)
    else:
        account_exists.expected_yield = expected_yield
        account_exists.total_shares = total_shares
        account_exists.total_bonds = total_bonds
        account_exists.total_etf = total_etf
        account_exists.total_currencies = total_currencies
        account_exists.total_futures = total_futures
        account_exists.type = type
    db.session.commit()
