from data import db_session
from flask import Flask, render_template, redirect, request
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


@app.route("/hub")
def hub():
    data = poisk_st.poisk_statbi()
    return render_template("templates/hub.html", menu=data)


@app.route('/register', methods=['POST', 'GET'])
def regster():
    if request.method == 'POST':
        register.regiister(request.form)
    return render_template("templates/register.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        Login.Login(request.form)
    return render_template("templates/login.html")


@app.route('/moder')  # TODO продумать как была так, чтобы входить мог только модер и сделать страницу
def loginM():
    return render_template("")


@app.route('/stat/<id>')  # TODO страница со статьёй
def Statba(id):
    data = poisk_st(id)
    return render_template("templates/stat", nazv=data[1], text=data[2])


def main():
    db_session.global_init("DataBase.sqlite")
    app.run()


if __name__ == '__main__':
    main()
