from webapp.dashboard.models import db, Instrument

def save_assets(figi, tiker, type, name, currency, sector):
    assets = Instrument(figi=figi,
                    tiker=tiker, type=type, name=name, currency=currency, sector=sector)
    db.session.add(assets)
    db.session.commit()