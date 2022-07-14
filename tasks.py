from celery import Celery
from webapp import create_app
from webapp.news.parsers import investing

flask_app = create_app()
celery_app = Celery('tasks', broker='redis://localhost:6379/0')

@celery_app.task
def investing_snippets():
    with flask_app.app_context():
         investing.get_investing_snippets()

@celery_app.task
def investing_content():
    with flask_app.app_context():
         investing.get_news_content ()