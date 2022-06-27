from getpass import getpass
import sys

from webapp import create_app
from webapp.model import db, User

app = create_app()

with app.app_context():
    username = input('Name: ')

    if User.query.filter(User.username == username).count():
        print('This name is already taken')
        sys.exit(0)

    password = getpass('Password: ')
    password2 = getpass('Repeat password: ')
    
    if not password == password2:
        print('Pass doesnt match')
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print('User with id {} added'.format(new_user.id))