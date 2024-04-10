import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    login = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=True)


class Statbi(SqlAlchemyBase):
    __tablename__ = 'Stati'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    URL_image = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    Text = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    IdPols = sqlalchemy.Column(sqlalchemy.String, nullable=True)