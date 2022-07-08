from flask import abort, Blueprint, render_template
from webapp.news.model import News

blueprint = Blueprint('news', __name__, url_prefix='/news')

@blueprint.route('/')
def index():
    context = {'page_title': 'News'}

    context['news'] = News.query.filter(News.text.isnot(None)).order_by(News.published.desc()).all()
    return render_template('news/pages-news.html', context=context)

@blueprint.route('/news/<int:news_id>')
def single_news(news_id):
    context = {}
    context['news'] = News.query.filter(News.id == news_id).first()
    if not context['news']:
        abort(404)
    return render_template('news/pages-single-news.html', context=context)

