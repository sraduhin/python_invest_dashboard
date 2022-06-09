import os

basedir = os.path.dirname(__file__)

CURRENCIES_API_KEY = "PHYlozjcZ5z6aDwXStIkjSYq40KWfRDi"
#TINKOFF_API_KEY = "t.KuJkD0UfDsdvKMYCE7iAxDFEBp9Wn46EcKUK3CVGFqnsT_EqHKxuqByOWzT-zCYBAKKJz0VYOJ1LX5fMHnIO0g" # IIS
TINKOFF_API_KEY = "t.wIZv11DNqtEOXsPEkDKwSr6RWQ2vZBc-QQOpPJv6MMNQpg8vn73ccRdVQ-tsvMFl3ED60O9kBu46NohrqL7_TA" # ALL
CURRENCIES_URL = "https://api.apilayer.com/fixer/latest"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')