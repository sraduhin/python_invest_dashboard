from webapp.model import db, Shares

def save_shares(name, figi, tiker, classCode, exchange, currency):
    shares = Shares(name=name, figi=figi, tiker=tiker,
                                classCode=classCode, exchange=exchange,
                                currency=currency)
    db.session.add(shares)
    db.session.commit()