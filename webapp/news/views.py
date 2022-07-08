from flask import Blueprint, render_template
from webapp.news.model import News

from flask_login import current_user

blueprint = Blueprint('news', __name__)

@blueprint.route('/')
def index():
    title = 'News'
    return render_template('dashboard/index.html', page_title=title)

