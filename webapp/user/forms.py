from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from webapp.user.models import User

class LoginForm(FlaskForm):
    username = StringField('Your username',validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Your password',validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Remember me', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Submit',render_kw={"class":"btn btn-primary"})

class RegistrationForm(FlaskForm):
    name = StringField('Your Name',validators=[DataRequired()], render_kw={"class": "form-control"})
    username = StringField('Your username',validators=[DataRequired()], render_kw={"class": "form-control"})
    email = StringField('Your email',validators=[DataRequired(), Email()], render_kw={"class": "form-control"})
    password = PasswordField('Your password',validators=[DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField('Repeat password please',validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control"})
    api_key = StringField('Fill your API Key',validators=[], render_kw={"class": "form-control"})
    submit = SubmitField('Create Account',render_kw={"class":"btn btn-primary"})

    def validate_username(self, username):
        user_count = User.query.filter_by(username=username.data).count()
        if user_count > 0:
            raise ValidationError('This username already exist')

    def validate_email(self, email):
        mail_count = User.query.filter_by(email=email.data).count()
        if mail_count > 0:
            raise ValidationError('This email already taken')
