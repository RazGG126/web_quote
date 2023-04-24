import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Quote(SqlAlchemyBase):
    __tablename__ = 'quotes'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    author = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    likes_number = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, default=0)
    comments_number = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, default=0)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))

    user = orm.relationship('User')
    comments = orm.relationship('Comment', back_populates='quote')
    likes = orm.relationship('Like', back_populates='quote')