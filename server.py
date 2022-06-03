from locale import currency
from flask import Flask, render_template
from currencies import get_currencies

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Invest DashBoard'
    currencies_code = 'USD%2C%20EUR%2C%20GBP%2C%20JPY%2C%20TRY'
    base_currency = 'RUB'
    tikers = currencies_code.split('%2C%20')
    # Сохраним запросы API
    #currencies = get_currencies(currencies_code, base_currency)
    currencies = {'USD': 0.015873, 'EUR': 0.014775, 'GBP': 0.012637, 'JPY': 2.071604, 'TRY': 0.26239}
    return render_template('index.html', page_title=title, currencies=currencies, tikers=tikers, base_currency=base_currency)

if __name__ == '__main__':
    app.run(debug=True)