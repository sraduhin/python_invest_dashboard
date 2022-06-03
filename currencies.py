import requests
import settings

# Запрашиваем валютные пары: RUBUSD, RUBEUR, RUBGBP, RUBJPY, RUBTRY
# Документация https://apilayer.com/marketplace/fixer-api?preview=true#
def get_currencies(symbols, base):
    url = settings.currencies_URL
    params = {
        'symbols': symbols,
        'base': base
    }
    payload = {}
    headers= {
    "apikey": settings.currencies_API_KEY
    }

    try:
        result = requests.get(url, params=params, headers=headers, data = payload)
        result.raise_for_status()
        currencies = result.json()
        if currencies['success'] == True:
            try:
                return currencies['rates']
            except(IndexError, TypeError):
                return False
    except(requests.RequestException, ValueError):
        print('Network error')
        return False
    return False

if __name__ == '__main__':
    print(get_currencies('USD%2C%20EUR%2C%20GBP%2C%20JPY%2C%20TRY', 'RUB')) 
