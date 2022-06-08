from locale import currency
from flask import Flask, render_template
from webapp.currencies import get_currencies
from webapp.invest_accounts import get_portfolio

def create_app():
    """
    run app
    Mac: export FLASK_APP=webapp && export FLASK_ENV=development && flask run
    Win: set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run"""
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        title = 'Invest DashBoard'
        currencies_code = 'USD%2C%20EUR%2C%20GBP%2C%20JPY%2C%20TRY'
        base_currency = 'RUB'
        tikers = currencies_code.split('%2C%20')
        # Сохраним запросы API
        #currencies = get_currencies(currencies_code, base_currency)
        currencies = {'USD': 0.015873, 'EUR': 0.014775, 'GBP': 0.012637, 'JPY': 2.071604, 'TRY': 0.26239}
        
        portfolio = get_portfolio()
        return render_template('index.html', page_title=title, currencies=currencies, tikers=tikers, base_currency=base_currency, portfolio=portfolio)


    return app