import os

from dotenv import load_dotenv

from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from quote_web.data import db_session

app = Flask(__name__)

load_dotenv()

login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db_session.global_init("quote_web/db/quotes.db")

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASSWORD')

mail = Mail(app)

from quote_web import routes