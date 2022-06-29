from webapp.portfolio.queries import get_position_row


if __name__ == '__main__':
    from webapp import create_app
    app = create_app()
    with app.app_context():
        get_position_row('2000377867')
