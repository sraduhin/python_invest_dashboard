import requests
import webapp.config as config


def get_currencies(base, labels=['USD', 'EUR', 'GBP', 'JPY', 'TRY']):
    base = base.upper()
    # Сохраним запросы API
    # currencies = {'USD': 0.015873, 'EUR': 0.014775, 'GBP': 0.012637, 'JPY': 2.071604, 'TRY': 0.26239}
    # return currencies
    """
    Фукнция должна вернуть соотношение валютных пар RUBUSD, RUBEUR, RUBGBP, RUBJPY, RUBTRY
    в формате:
    {
        "base": "RUB",
        "date": "2022-06-04",
        "rates": {
            "EUR": 0.014723,
            "GBP": 0.012636,
            "JPY": 2.064721,
            "TRY": 0.259868,
            "USD": 0.015783
        },
        "success": true,
        "timestamp": 1654345755
        }
    Документация к API https://apilayer.com/marketplace/fixer-api?preview=true#

    """
    url = config.CURRENCIES_URL
    labels = '%2C%20'.join(labels)
    params = {
        'symbols': labels,
        'base': base
    }
    payload = {}
    headers = {"apikey": config.CURRENCIES_API_KEY}
    try:
        result = requests.get(url, params=params, headers=headers, data=payload)
        result.raise_for_status()
        #status_code = response.status_code
        currencies = result.json()
        if currencies.get('success') is True:
            return currencies.get('rates')
    except(requests.RequestException, ValueError):
        print('Network error')
        return False
    return False


if __name__ == '__main__':
    print(get_currencies('RUB'))

