from webapp import create_app
from webapp.model import Portfolio, Position, Instrument

app = create_app()
with app.app_context():
    def get_positions_row(portfolio_id):
        securities = Position.query.join(Portfolio, Position).filter()  #  fuuuuck

    if __name__ == '__main__':
        get_positions_row(1)
        #  get_positions_row(2)
