from webapp import create_app
from webapp.portfolio.get_assets import get_assets
from webapp.portfolio.get_portfolios import get_portfolios
from webapp.portfolio.get_positions import get_positions

app = create_app()
with app.app_context():
    get_assets()
    get_portfolios()
    get_positions()
