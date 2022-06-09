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
            portfolio = client.operations.get_portfolio(account_id=account)
            portfolio = portfolio.positions
            #positions = client.operations.get_positions(account_id=account)
            #positions = positions.securities
            for position in portfolio:
                figi = position.figi
                instrument_type = position.instrument_type
                currency = position.current_price.currency
                quantity = position.quantity.units + position.quantity.nano / 1000000000
                expected_yield = position.expected_yield.units + position.expected_yield.nano / 1000000000
                average_position_price_pt = position.average_position_price_pt.units + position.average_position_price_pt.nano / 1000000000
                quantity_lots = position.quantity_lots.units + position.quantity_lots.nano / 1000000000
                average_position_price = position.average_position_price.units + position.average_position_price.nano / 1000000000
                current_nkd = position.current_nkd.units + position.current_nkd.nano / 1000000000
                current_price = position.current_price.units + position.current_price.nano / 1000000000
                average_position_price_fifo = position.average_position_price_fifo.units + position.average_position_price_fifo.nano / 1000000000
                save_securities(figi, instrument_type, currency, quantity, average_position_price,
                                expected_yield, current_nkd, average_position_price_pt, current_price,
                                average_position_price_fifo, quantity_lots)
            """for position in positions:
                figi = position.figi
                blocked = position.blocked
                balance = position.balance
                save_securities(figi, blocked, balance)"""
                
def save_securities(figi, instrument_type, currency, quantity, average_position_price,
                    expected_yield, current_nkd, average_position_price_pt, current_price,
                    average_position_price_fifo, quantity_lots):
    position_securities = Securities(figi=figi, instrument_type=instrument_type,
                                    currency=currency, quantity=quantity,
                                    average_position_price=average_position_price,
                                    expected_yield=expected_yield, current_nkd=current_nkd,
                                    average_position_price_pt=average_position_price_pt,
                                    current_price=current_price,
                                    average_position_price_fifo=average_position_price_fifo,
                                    quantity_lots=quantity_lots)
    db.session.add(position_securities)
    db.session.commit()