from webapp.model import db, Securities

def save_securities(account_id, figi, currency, name, tiker, class_code, exchange, amount, average_price,
                    expected_yield, current_nkd, current_price,
                    fifo, lots):
    position_securities = Securities(account_id=account_id, figi=figi, currency=currency,
                                    name=name, tiker=tiker, class_code=class_code, exchange=exchange, 
                                    amount=amount, average_price=average_price,
                                    expected_yield=expected_yield, current_nkd=current_nkd,
                                    current_price=current_price,
                                    fifo=fifo, lots=lots)
    db.session.add(position_securities)
    db.session.commit()