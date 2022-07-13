from flask import Blueprint, render_template, flash, redirect, url_for

from flask_login import current_user, login_user, logout_user

from webapp.db import db 

from webapp.dashboard.get_portfolios import get_portfolios
from webapp.dashboard.get_positions import get_positions
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users')

@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    title = "Authentication"
    form = LoginForm()
    return render_template('user/pages-login.html', page_title=title, form=form)

@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Welcome on site')
            get_portfolios()
            get_positions()
            return redirect(url_for('dashboard.index'))

    flash('Incorrect name or pass')
    return redirect(url_for('user.login'))

@blueprint.route('/logout')
def logout():
    logout_user()
    flash('Success logout')
    return redirect(url_for('dashboard.index'))

@blueprint.route('/register ')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.index'))
    title = "Registration" 
    form = RegistrationForm()
    return render_template('user/pages-register.html', page_title=title, form=form)

@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(name=form.name.data, username=form.username.data, email=form.email.data, api_key=form.api_key.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Successful')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Check {}: {}'.format(getattr(form, field).label.text, error))
    return redirect(url_for('user.register'))
