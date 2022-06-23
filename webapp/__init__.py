from flask import Flask, render_template

from webapp.model import db, Position
from queries import get_position_row
import json


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
        securities = get_position_row('2000377867')
        historycal_portfolio_data = {'Monday': 1000, "Tuesday": 900, "Wednesday": 1230, "Thursday": 1400, "Friday": 1800, "Saturday": 1700, "Sunday": 1500}
        labels = list(historycal_portfolio_data.keys())
        values = list(historycal_portfolio_data.values())
        return render_template('index.html', page_title=title, currencies=currencies, tikers=tikers, base_currency=base_currency, securities=securities, labels=labels, values=values)
    return app
