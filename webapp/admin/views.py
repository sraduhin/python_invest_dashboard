from flask import Blueprint
from webapp.user.decorators import admin_required

from flask_login import current_user

blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@blueprint.route('/')
@admin_required
def admin_index():
    return 'Привет админ'

