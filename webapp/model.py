from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Shares(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=True)
    figi = db.Column(db.String, nullable=False)
    tiker = db.Column(db.String, nullable=True)
    classCode = db.Column(db.String, nullable=True)
    exchange = db.Column(db.String, nullable=True)
    currency = db.Column(db.String, nullable=True)
    securities = db.relationship('Securities', backref='shares')

    def __repr__(self):
        return '<Shares {} {}>'.format(self.figi, self.tiker)

class Portfolios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    data = db.Column(db.Boolean, nullable=False)
    expected_yield = db.Column(db.Float, nullable=True)
    total_currencies = db.Column(db.Float, nullable=True)
    total_shares = db.Column(db.Float, nullable=True)
    total_etf = db.Column(db.Float, nullable=True)
    total_bonds = db.Column(db.Float, nullable=True)
    total_futures = db.Column(db.Float, nullable=True)
    securities = db.relationship('Securities', backref='portfolio')

    def __repr__(self):
        return '<Portfolios {} {}>'.format(self.id, self.type)
        
class Securities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    figi = db.Column(db.String, db.ForeignKey('shares.figi'))
    account_id = db.Column(db.Integer, db.ForeignKey('portfolio.account_id'))
    amount = db.Column(db.Float, nullable=False)
    average_price = db.Column(db.Float, nullable=False)
    expected_yield = db.Column(db.Float, nullable=False)
    current_nkd = db.Column(db.Float, nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    fifo = db.Column(db.Float, nullable=False)
    lots = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<securities {} {}>'.format(self.figi, self.amount)

