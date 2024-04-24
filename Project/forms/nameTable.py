from flask_login import LoginManager
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms import BooleanField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired

login_manager = LoginManager()


# (login_manager.init_app(app))


class LoginForm(FlaskForm):
    Login = EmailField('Почта', validators=[DataRequired()])
    Password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegisterForm(FlaskForm):
    Login = EmailField('Почта', validators=[DataRequired()])
    Password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')


class NewStat(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    url_image = FileField('Загрузить изображение', validators=[DataRequired()])
    text = TextAreaField('Текст статьи', validators=[DataRequired()])
    password = FileField('Загрузить изображение', validators=[DataRequired()])
    submit = SubmitField('Сохранить')
