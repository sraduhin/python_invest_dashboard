from flask import Flask, render_template, flash, redirect, url_for
from queries import get_position_row
from flask_login import LoginManager, current_user, login_required, login_user, logout_user

from webapp.forms import LoginForm
from webapp.model import db, User

def create_app():
    """
    run app
    Mac: export FLASK_APP=webapp && export FLASK_ENV=development && flask run
    Win: set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run"""
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

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

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = "Authentication"
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Welcome on site')
                return redirect(url_for('index'))

        flash('Incorrect name or pass')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Success logout')
        return redirect(url_for('index'))

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет админ'
        else:
            return 'Ты не админ!'    

    return app