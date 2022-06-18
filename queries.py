from webapp import create_app
from webapp.model import Portfolios

app = create_app()
with app.app_context():

    def securities_by_account(account_id):
        securities = Portfolios.query.filter(Portfolios.account_id == account_id).all()
        return securities

if __name__ == '__main__':
    print(securities_by_account('2109627600'))