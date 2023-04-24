import os

from quote_web import config

from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from quote_web.data import db_session

app = Flask(__name__)


login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = config.SECRET_KEY
db_session.global_init("quote_web/db/quotes.db")

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = config.EMAIL_USER
app.config['MAIL_PASSWORD'] = config.EMAIL_PASSWORD

mail = Mail(app)

from quote_web import routes