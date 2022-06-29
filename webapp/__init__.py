from flask import Flask
from flask_login import LoginManager
from webapp.user.views import blueprint as user_blueprint
from webapp.admin.views import blueprint as admin_blueprint
from webapp.portfolio.views import blueprint as portfolio_blueprint
from webapp.currency.views import blueprint as currency_blueprint
from webapp.db import db
from webapp.user.models import User

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(currency_blueprint)
    app.register_blueprint(portfolio_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app