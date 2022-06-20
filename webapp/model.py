from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.Integer, nullable=True)
    expected_yield = db.Column(db.Float, nullable=True)
    total_shares = db.Column(db.Float, nullable=True)
    total_bonds = db.Column(db.Float, nullable=True)
    total_etf = db.Column(db.Float, nullable=True)
    total_currencies = db.Column(db.Float, nullable=True)
    total_futures = db.Column(db.Float, nullable=True)
    type = db.Column(db.String, nullable=False)
    position = db.relationship('Position', backref='portfolio', lazy=True)

    def __repr__(self):
        return '<Portfolio {} {}>'.format(self.account, self.expected_yield)

class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('portfolio.account'), nullable=False)
    figi_id = db.Column(db.String, db.ForeignKey('instrument.figi'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    expected_yield = db.Column(db.Float, nullable=False)
    average_price = db.Column(db.Float, nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    lots = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Position {} {}>'.format(self.figi, self.current_price)

class Instrument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    figi = db.Column(db.String, nullable=True)
    tiker = db.Column(db.String, nullable=True)
    type = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    currency = db.Column(db.String, nullable=False)
    position = db.relationship('Position', backref='instrument', lazy=True)

    def __repr__(self):
        return '<Position {} {}>'.format(self.tiker, self.name)
