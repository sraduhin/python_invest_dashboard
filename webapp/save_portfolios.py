from webapp.model import db, Portfolio


def save_portfolios(account, type, expected_yield,total_shares,
                    total_bonds, total_etf, total_currencies, total_futures):
    portfolios = Portfolio(account=account, type=type,
                            expected_yield=expected_yield, total_currencies=total_currencies,
                            total_shares=total_shares, total_etf=total_etf, total_bonds=total_bonds,
                            total_futures=total_futures)
    db.session.add(portfolios)
    db.session.commit()
