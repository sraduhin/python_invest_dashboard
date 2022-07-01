from webapp.dashboard.currencies import get_currencies
def normalize_floatings(obj):
    divisor = 1000000000  # (units=5, nano=300000000) => units + nano / divisor = 5.30
    return obj.units + obj.nano / divisor

def get_price_in_base_currency(value, base_currency='USD'):
    base_currency = base_currency.upper()
    if base_currency == 'RUB':
        return value
    else:
        return value * get_currencies('RUB')[base_currency]

def get_total_amount(price, amount):
    return price * amount
