""" тут пока нечего смотреть """
from webapp import create_app
from webapp.model import Portfolio, Position, Instrument
app = create_app()
with app.app_context():
    def get_positions_row(portfolio_id):
        securities = Position.query.join(Portfolio, Position).filter()  #  fuuuuck

    def get_portfolio_id():
        portfolios = Portfolio.query.all()
        for _ in portfolios:
            print(_.account_id)
        

    if __name__ == '__main__':
        get_portfolio_id()
        #  get_positions_row(2)
