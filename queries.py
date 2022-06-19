from webapp import create_app
from webapp.model import Portfolios, Securities

app = create_app()
with app.app_context():

    def securities_by_account(account_id):
        account = Portfolios.query.filter(Portfolios.account_id == account_id).first()
        security_list = []
        if account:
            return Securities.query.all()

    if __name__ == '__main__':
        print(securities_by_account('2109627600'))