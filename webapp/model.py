from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Securities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    figi = db.Column(db.String, unique=True, nullable=False)
    blocked = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<securities {} {}>'.format(self.figi, self.balance)