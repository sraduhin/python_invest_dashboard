from webapp.model import db, Portfolios


def save_portfolios(account_id, type, expected_yield, total_currencies,
                    total_shares, total_etf, total_bonds, total_futures):
    portfolios = Portfolios(account_id=account_id, type=type,
                            expected_yield=expected_yield, total_currencies=total_currencies,
                            total_shares=total_shares, total_etf=total_etf, total_bonds=total_bonds,
                            total_futures=total_futures)
    db.session.add(portfolios)
    db.session.commit()
