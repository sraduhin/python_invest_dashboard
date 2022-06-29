from flask import Blueprint, render_template
from webapp.portfolio.queries import get_position_row

blueprint = Blueprint('securities', __name__)

@blueprint.route('/')
def index():
    title = 'Securities'
    account_id = '2000377867'
    securities = get_position_row(account_id)
    #historycal_portfolio_data = {'Monday': 1000, "Tuesday": 900, "Wednesday": 1230, "Thursday": 1400, "Friday": 1800, "Saturday": 1700, "Sunday": 1500}
    #labels = list(historycal_portfolio_data.keys())
    #values = list(historycal_portfolio_data.values())
    return render_template('portfolio/index.html', account_id=account_id, securities_block_title=title, securities=securities)
