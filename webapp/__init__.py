from flask import Flask, render_template

from webapp.model import db, Securities


def create_app():
    """
    run app
    Mac: export FLASK_APP=webapp && export FLASK_ENV=development && flask run
    Win: set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run"""
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title = 'Invest DashBoard'
        tikers = ['USD', 'EUR', 'GBP', 'JPY', 'TRY']
        base_currency = 'RUB'
        # Сохраним запросы API
        # currencies = get_currencies('%2C%20'.join(tikers), base_currency)
        currencies = {'USD': 0.015873, 'EUR': 0.014775, 'GBP': 0.012637, 'JPY': 2.071604, 'TRY': 0.26239}
        securities = Securities.query.all()
        return render_template('index.html', page_title=title, currencies=currencies, tikers=tikers, base_currency=base_currency, securities=securities)
    return app
