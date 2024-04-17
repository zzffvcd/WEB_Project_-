import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'Pols'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    login = sqlalchemy.Column(sqlalchemy.TEXT, nullable=True)
    password = sqlalchemy.Column(sqlalchemy.TEXT, nullable=True)


class Statbi(SqlAlchemyBase):
    __tablename__ = 'Statbi'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.TEXT, nullable=True)
    URL_image = sqlalchemy.Column(sqlalchemy.TEXT, nullable=False)
    Text = sqlalchemy.Column(sqlalchemy.TEXT, nullable=True)
    IdPols = sqlalchemy.Column(sqlalchemy.TEXT, nullable=True)