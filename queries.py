from webapp.dashboard.queries import get_position_row, get_balance_by_account


if __name__ == '__main__':
    from webapp import create_app
    app = create_app()
    with app.app_context():
        #get_position_row('2000377867')
        get_balance_by_account('2000377867')
