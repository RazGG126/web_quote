import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Like(SqlAlchemyBase):
    __tablename__ = 'likes'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    quote_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("quotes.id"))
    user = orm.relationship('User')
    quote = orm.relationship('Quote')

    def __repr__(self):
        return f"{self.content} {self.user_id} {self.quote_id}"