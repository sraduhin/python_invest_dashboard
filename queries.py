from webapp.portfolio.models import db, Portfolio

    
    
def get_position_row(account_id):
    portfolio = Portfolio.query.filter(Portfolio.account_id == account_id).first()
    position_list = []
    if portfolio:
        for position in portfolio.position:
            name = position.instrument.name
            tiker = position.instrument.tiker
            amount = position.amount
            average_price = position.average_price
            total = amount * average_price
            current_price = amount * position.current_price
            expected_yield = position.expected_yield
            position_list.append({'Name':name, 'Tiker':tiker, 'Amount':amount, 'Average price':average_price,
                            'Total':total, 'Current price':current_price, 'Expected yield':expected_yield})
    return position_list


if __name__ == '__main__':
    get_position_row('2000377867')
