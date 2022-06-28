from webapp.portfolio.models import db, Instrument

def save_assets(figi, tiker, type, name, currency):
    assets = Instrument(figi=figi,
                    tiker=tiker, type=type, name=name, currency=currency)
    db.session.add(assets)
    db.session.commit()