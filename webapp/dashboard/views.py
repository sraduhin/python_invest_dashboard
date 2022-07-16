from flask import Blueprint, render_template
from webapp.dashboard.models import Portfolio
from webapp.dashboard.queries import get_position_row, get_balance_by_account, get_money_by_sectors, get_currencies_row
from webapp.dashboard.get_assets import get_assets
from flask_login import current_user

blueprint = Blueprint('dashboard', __name__)

@blueprint.route('/<int:account_id>') # 2000377867  2109627600
#@blueprint.route('/')
def index(account_id):
#def index():
    get_assets()

    context = {'page_title': 'InvestDashboard'}

    currencies_block_title = 'Currencies'
    base_currency = 'RUB'
    context['currencies'] = {}
    context['currencies']['title'] = currencies_block_title
    context['currencies']['base_currency'] = base_currency
    context['currencies']['positions'] = get_currencies_row(base_currency)
    
    if current_user.is_authenticated:
        securities_block_title = 'Securities'
        accounts = Portfolio.query.filter(Portfolio.user_id==current_user.id).all()
        context['securities'] = {}
        context['securities']['title'] = securities_block_title
        context['securities']['account_id'] = account_id
        context['securities']['accounts'] = accounts
        context['securities']['positions'] = get_position_row(account_id)

        context['portfolio'] = {}
        context['portfolio']['balances'] = get_balance_by_account(account_id)

        round_diagramm_title = 'Sectors'
        context['sectors'] = {}
        context['sectors']['title'] = round_diagramm_title
        context['sectors']['account_id'] = account_id
        context['sectors']['percentage'] = get_money_by_sectors(account_id)

    return render_template('dashboard/index.html', context=context)
