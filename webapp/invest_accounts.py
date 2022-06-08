from tinkoff.invest import Client
from flask import current_app
from webapp.model import db, Securities

def get_portfolio():
    TOKEN = current_app.config['TINKOFF_API_KEY']
    with Client(TOKEN) as client:
        accounts = client.users.get_accounts().__dict__['accounts'] # Приводим к виду [Account(...), Account(...), ...]
        #print(client.operations.get_portfolio(account_id='2109627600'))

    
        def findAccountsWithReadOnlyLevel(accounts):
            """
            Фукнция ищет среди портфелей счета с полным ACCOUNT_ACCESS_LEVEL_FULL_ACCESS=1,
            либо read-only ACCOUNT_ACCESS_LEVEL_READ_ONLY=2 доступом
            """
            accounts_with_access = []
            for account in accounts:
                if account.access_level == 1 or account.access_level == 2:
                    accounts_with_access.append(account.id)
            return accounts_with_access
        accounts_with_access = findAccountsWithReadOnlyLevel(accounts)
        for account in accounts_with_access:
            #portfolio = client.operations.get_portfolio(account_id=account)
            positions = client.operations.get_positions(account_id=account)
            positions = positions.securities
            #return positions
            for position in positions:
                figi = position.figi
                blocked = position.blocked
                balance = position.balance
                save_securities(figi, blocked, balance)

def save_securities(figi, blocked, balance):
    position_securities = Securities(figi=figi, blocked=blocked, balance=balance)
    db.session.add(position_securities)
    db.session.commit()