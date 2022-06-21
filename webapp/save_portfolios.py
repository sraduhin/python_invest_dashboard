from webapp.model import db, Portfolio


def save_portfolios(account_id, expected_yield,total_shares,
                    total_bonds, total_etf, total_currencies, total_futures, type):
    portfolios = Portfolio(account_id=account_id, expected_yield=expected_yield, total_shares=total_shares,
                            total_bonds=total_bonds, total_etf=total_etf,
                            total_currencies=total_currencies,
                            total_futures=total_futures, type=type)
    db.session.add(portfolios)
    db.session.commit()
