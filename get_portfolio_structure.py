from webapp import create_app
from webapp.invest_accounts import get_portfolio

app = create_app()
with app.app_context():
    get_portfolio()