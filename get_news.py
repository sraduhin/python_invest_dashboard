from webapp import create_app
from webapp.news.parsers import investing

app = create_app()
with app.app_context():
    investing.get_investing_snippets()
    investing.get_news_content()