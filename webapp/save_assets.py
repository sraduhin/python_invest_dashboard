from webapp.model import db, Assets

def save_assets(name, figi, type, tiker, class_code):
    assets = Assets(name=name, figi=figi, type=type,
                    tiker=tiker, class_code=class_code)
    db.session.add(assets)
    db.session.commit()