from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Securities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    figi = db.Column(db.String, nullable=False)# make unique true
    currency = db.Column(db.String, nullable=False)
    instrument_type = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Float , nullable=False)
    average_position_price = db.Column(db.Float, nullable=False)
    expected_yield = db.Column(db.Float, nullable=False)
    current_nkd = db.Column(db.Float, nullable=False)
    average_position_price_pt = db.Column(db.Float, nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    average_position_price_fifo = db.Column(db.Float, nullable=False)
    quantity_lots = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<securities {} {}>'.format(self.figi, self.balance)