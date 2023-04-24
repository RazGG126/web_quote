import datetime
import sqlalchemy
import jwt
from sqlalchemy import orm
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .db_session import SqlAlchemyBase

from quote_web import app


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    nick_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=False)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    user_photo = sqlalchemy.Column(sqlalchemy.String)

    first_blob_color = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    second_blob_color = sqlalchemy.Column(sqlalchemy.String, nullable=False)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)

    quotes = orm.relationship("Quote", back_populates='user')
    likes = orm.relationship("Like", back_populates='user')
    comments = orm.relationship("Comment", back_populates='user')

    def __repr__(self):
        return f"{self.id}: {self.name} {self.surname} {self.email}"

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
    
    def generate_token(self):
        token = jwt.encode({'user_id': self.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, app.config['SECRET_KEY'])
        return token

    @staticmethod
    def verify_token(token):
        try:
            user_id = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])['user_id']
        except:
            return None
        return user_id

        
        
