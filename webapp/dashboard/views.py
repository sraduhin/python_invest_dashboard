from flask import Blueprint, render_template
from webapp.dashboard.queries import get_position_row, get_balance_by_account
from webapp.dashboard.currencies import get_currencies

blueprint = Blueprint('securities', __name__)

@blueprint.route('/')
def index():
    context = {}

    securities_block_title = 'Securities'
    account_id = '2000377867'
    context['securities'] = {}
    context['securities']['title'] = securities_block_title
    context['securities']['account_id'] = account_id
    context['securities']['positions'] = get_position_row(account_id)

    currencies_block_title = 'Currencies'
    base_currency = 'RUB'
    context['currencies'] = {}
    context['currencies']['title'] = currencies_block_title
    context['currencies']['base_currency'] = base_currency
    context['currencies']['positions'] = get_currencies(base_currency)

    context['portfolio'] = {}
    context['portfolio']['balances'] = get_balance_by_account(account_id)

    return render_template('dashboard/index.html', context=context)
