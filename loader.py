from webapp import create_app
from webapp.get_securities import get_securities
from webapp.get_shares import get_shares
from webapp.get_portfolios import get_portfolios

app = create_app()
with app.app_context():
    get_securities()
    get_shares()
    get_portfolios()