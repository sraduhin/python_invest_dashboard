from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.String, nullable=True)
    expected_yield = db.Column(db.Float, nullable=True)
    total_shares = db.Column(db.Float, nullable=True)
    total_bonds = db.Column(db.Float, nullable=True)
    total_etf = db.Column(db.Float, nullable=True)
    total_currencies = db.Column(db.Float, nullable=True)
    total_futures = db.Column(db.Float, nullable=True)
    type = db.Column(db.String, nullable=False)
    position = db.relationship('Position', backref='portfolio', lazy=True)

    def __repr__(self):
        return '<Portfolio {} {}>'.format(self.account_id, self.expected_yield)


class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'), index=True, nullable=False)
    instrument_id = db.Column(db.String, db.ForeignKey('instrument.id'), index=True, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    expected_yield = db.Column(db.Float, nullable=False)
    average_price = db.Column(db.Float, nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    lots = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Position {} {}>'.format(self.amount, self.current_price)


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


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return '<User {}>'.format(self.username)
