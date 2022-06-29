from webapp.portfolio.models import Portfolio


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
    print(position_list)
    return position_list
  

