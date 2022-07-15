from webapp.dashboard.queries import get_position_row, get_balance_by_account, get_money_by_sectors, get_currencies_row
from webapp.dashboard.currencies import get_currencies


if __name__ == '__main__':
    from webapp import create_app
    app = create_app()
    with app.app_context():
        #get_position_row('2000377867')
        #get_balance_by_account('2000377867')
        #get_money_by_sectors('2000377867')
        #get_currencies_row('RUB')
        
        print(get_currencies('RUB'))
