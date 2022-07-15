from webapp.dashboard.models import Portfolio
from webapp.dashboard.normalize import get_price_in_base_currency
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
            position_list.append({'Name': name, 'Tiker': tiker, 'Amount': amount, 'Average price': average_price,
                            'Total': total, 'Current price': current_price, 'Expected yield': expected_yield})
    return position_list


def get_balance_by_account(account_id, currency='usd'):
    portfolio = Portfolio.query.filter(Portfolio.account_id == account_id).first()
    balance = portfolio.total_shares + portfolio.total_bonds + portfolio.total_etf + portfolio.total_currencies + portfolio.total_futures
    profit = balance * portfolio.expected_yield / 100
    portfolio_balances = {'balance': balance, 'profit': profit}
    portfolio_balances = {key: round(get_price_in_base_currency(value, currency), 2) for (key, value) in portfolio_balances.items()}
    portfolio_balances['profit_by_percent'] = round((profit / balance * 100), 2)
    print(portfolio_balances)
    return portfolio_balances


def get_money_by_sectors(account_id, currency='usd'):
    positions = Portfolio.query.filter(Portfolio.account_id == account_id).first().position
    '''нужно достать все акции instrument.type = shares из конкретного портфеля Portfolio.account_id и вывести
    Position.amount, Instrument.sector, Instrument.currency'''
    money_by_sectors = {}
    for position in positions:
        sector = position.instrument.sector
        if sector != None:
            if position.instrument.currency != currency:
                position_value = get_price_in_base_currency(position.current_price, currency) * position.amount
            else:
                position_value = position.current_price * position.amount
            position_value = round(position_value, 2)
            if sector in money_by_sectors:
                money_by_sectors[sector] += position_value
            else:
                money_by_sectors[sector] = position_value
    money_by_sectors_list = []
    for key, value in money_by_sectors.items():
        money_by_sectors_list.append({'value': value, 'name': key})
    return money_by_sectors_list


def get_currencies_row(base_currency):
    row = get_currencies(base_currency)
    print(row)
    row = {key: round(1/ value, 2) for (key, value) in row.items()}
    print(row)
    return row

