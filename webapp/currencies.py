import requests
import webapp.config as config

def get_currencies(symbols, base):
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
    url = config.currencies_URL
    params = {
        'symbols': symbols,
        'base': base
    }
    payload = {}
    headers= {
    "apikey": config.currencies_API_KEY
    }

    try:
        result = requests.get(url, params=params, headers=headers, data = payload)
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
    print(get_currencies('USD%2C%20EUR%2C%20GBP%2C%20JPY%2C%20TRY', 'RUB')) 
