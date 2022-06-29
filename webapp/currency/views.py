from flask import Blueprint, render_template
#from webapp.currency.currencies import get_currencies

blueprint = Blueprint('currencies', __name__)

@blueprint.route('/')
def index():
    title = 'Currencies'
    base_currency = 'RUB'
    # Сохраним запросы API
    # currencies = get_currencies('%2C%20'.join(tikers), base_currency)
    currencies = {'USD': 0.015873, 'EUR': 0.014775, 'GBP': 0.012637, 'JPY': 2.071604, 'TRY': 0.26239}
    labels = list(currencies.keys())
    return render_template('currency/index.html', currencies_block_title=title, currencies=currencies, base_currency=base_currency, labels=labels)
