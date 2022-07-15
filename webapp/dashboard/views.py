from flask import Blueprint, render_template
from webapp.dashboard.models import Portfolio
from webapp.dashboard.queries import get_position_row, get_balance_by_account, get_money_by_sectors, get_currencies_row, get_historycal_row
from webapp.dashboard.get_assets import get_assets
from flask_login import current_user

blueprint = Blueprint('dashboard', __name__)

@blueprint.route('/')
def index():
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
        account_id = Portfolio.query.filter(Portfolio.user_id==current_user.id).all()[0].account_id
        context['securities'] = {}
        context['securities']['title'] = securities_block_title
        context['securities']['account_id'] = account_id
        context['securities']['positions'] = get_position_row(account_id)

        context['portfolio'] = {}
        context['portfolio']['balances'] = get_balance_by_account(account_id)

        round_diagramm_title = 'Sectors'
        context['sectors'] = {}
        context['sectors']['title'] = round_diagramm_title
        context['sectors']['account_id'] = account_id
        context['sectors']['percentage'] = get_money_by_sectors(account_id)
        
        history_title = 'Historical portfolio data'
        context['history'] = {}
        context['history']['title'] = history_title
        context['history']['account_id'] = account_id
        context['history']['values'] = get_historycal_row()
        context['history']['dates'] = get_historycal_row()

    return render_template('dashboard/index.html', context=context)
