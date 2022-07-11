from webapp.dashboard.models import db, Portfolio, Position


def save_positions(portfolio_id, instrument_id, amount, expected_yield,
                    average_price, current_price):
    #query = Portfolio.query.filter(Portfolio.id == portfolio_id).first().position
    query = Position.query.filter(Position.instrument_id == instrument_id)
    query = query.join(Portfolio, Portfolio.id == portfolio_id)
    query = query.all()
    if not query:
        position_securities = Position(portfolio_id=portfolio_id, instrument_id=instrument_id,
                                    amount=amount, expected_yield=expected_yield,
                                    average_price=average_price, current_price=current_price)
        db.session.add(position_securities)

    print(query)
    db.session.commit()


"""def save_portfolios(account_id, expected_yield, total_shares,
                    total_bonds, total_etf, total_currencies, total_futures, type):
    account_exists = Portfolio.query.filter(Portfolio.account_id == account_id).first()
    if not account_exists:
        portfolios = Portfolio(account_id=account_id, expected_yield=expected_yield, total_shares=total_shares,
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
    db.session.commit()"""
