from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Securities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=True)
    tiker = db.Column(db.String, nullable=True)
    exchange = db.Column(db.String, nullable=True)
    currency = db.Column(db.String, nullable=True)
    class_code = db.Column(db.String, nullable=True)
    account_id = db.Column(db.Integer,)
    amount = db.Column(db.Float, nullable=False)
    average_price = db.Column(db.Float, nullable=False)
    expected_yield = db.Column(db.Float, nullable=False)
    current_nkd = db.Column(db.Float, nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    fifo = db.Column(db.Float, nullable=False)
    lots = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<securities {} {}>'.format(self.tiker, self.current_price)


class Portfolios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey(Securities.account_id))
    type = db.Column(db.Integer, nullable=False)
    expected_yield = db.Column(db.Float, nullable=True)
    total_currencies = db.Column(db.Float, nullable=True)
    total_shares = db.Column(db.Float, nullable=True)
    total_etf = db.Column(db.Float, nullable=True)
    total_bonds = db.Column(db.Float, nullable=True)
    total_futures = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return '<Portfolios {} {}>'.format(self.account_id, self.expected_yield)
