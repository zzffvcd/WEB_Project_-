from data import db_session
from flask import Flask, render_template, redirect
from forms.user import RegisterForm
from flask_login import LoginManager, current_user, login_required, logout_user, login_user
from data import db_session
from data import poisk_st
from data import register
from data import Login

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
db_sess = db_session.create_session()

if current_user.is_authenticated:
    news = db_sess.query(News).filter(
        (News.user == current_user) | (News.is_private != True))
else:
    news = db_sess.query(News).filter(News.is_private != True)


@app.route("/main")
def mainn():
    data = poisk_st.poisk_statbi()
    return render_template("templates/main.html", menu=data)


@app.route('/register')
def register():

    return render_template("templates/register.html")



@app.route('/login')
def login():
    return render_template("templates/login.html")


@app.route('/moder') #TODO продумать как была так, чтобы входить мог только модер и сделать страницу
def loginM():
    return render_template("")


@app.route('/stat') #TODO страница со статьёй
def Statba():
    return render_template("")


def main():
    db_session.global_init("DataBase.sqlite")
    app.run()


if __name__ == '__main__':
    main()