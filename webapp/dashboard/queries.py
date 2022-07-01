from webapp.dashboard.models import Portfolio
from webapp.dashboard.currencies import get_currencies


def get_position_row(account_id):
    portfolio = Portfolio.query.filter(Portfolio.account_id == account_id).first()
    position_list = []
    if portfolio:
        for position in portfolio.position:
            name = position.instrument.name
            tiker = position.instrument.tiker
            amount = position.amount
            average_price = round(position.average_price, 2)
            total = round(amount * average_price, 2)
            current_price = round(amount * position.current_price, 2)
            expected_yield = round(position.expected_yield, 2)
            position_list.append({'Name':name, 'Tiker':tiker, 'Amount':amount, 'Average price':average_price,
                            'Total':total, 'Current price':current_price, 'Expected yield':expected_yield})
    return position_list


def get_balance_by_account(account_id, currency='USD'):
    portfolio = Portfolio.query.filter(Portfolio.account_id == account_id).first()
    balance = portfolio.total_shares + portfolio.total_bonds + portfolio.total_etf + portfolio.total_currencies + portfolio.total_futures
    profit = balance * portfolio.expected_yield / 100
    portfolio_balances = {'balance': balance, 'profit': profit}
    if currency != 'RUB':
        portfolio_balances = {key: value * get_currencies('RUB')['USD'] for (key, value) in portfolio_balances.items()}
    return portfolio_balances

  

