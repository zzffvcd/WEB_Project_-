from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired

login_manager = LoginManager()
(login_manager.init_app(app)


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


if current_user.is_authenticated:
    news = db_sess.query(News).filter(
        (News.user == current_user) | (News.is_private != True))
else:
    news = db_sess.query(News).filter(News.is_private != True)
