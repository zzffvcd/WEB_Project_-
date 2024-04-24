import datetime
import sqlalchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'Pols'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    Login = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    Password = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    def set_password(self, password):
        self.Password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.Password, password)


class Statbi(SqlAlchemyBase):
    __tablename__ = 'Statbi'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.TEXT, nullable=True)
    URL_image = sqlalchemy.Column(sqlalchemy.TEXT, nullable=False)
    Text = sqlalchemy.Column(sqlalchemy.TEXT, nullable=True)
    IdPols = sqlalchemy.Column(sqlalchemy.TEXT, nullable=True)
