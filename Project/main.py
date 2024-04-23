from data import db_session
from flask import Flask, render_template, redirect, request
from forms.user import RegisterForm
from flask_login import LoginManager, current_user, login_required, logout_user, login_user
from data import db_session
from data import poisk_st
from data import register
from data import Login
from data import new_stat
from data.name_table import User, Statbi

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/hub")
def hub():
    data = poisk_st.poisk_statbi()
    return render_template("hub.html", menu=data)


@app.route("/newstat")
@login_required #TODO надо в new_stat.py добавить в БД написанный текст на этой странице
def newstat():
    data = newstat.new_stat()
    return render_template("hub.html", menu=data)


@app.route('/register', methods=['POST', 'GET'])
# TODO надо чтобы на эту страницу не мог зайти уже авторизованный. Ещё надо авторизовать пользователя.
def register():
    if request.method == 'POST':
        a = register.regiister(request.form)
        if a[1] == 0:
            login_user(user)
        else:

    return render_template("register.html", a=a)


@app.route('/login', methods=['POST', 'GET'])
# TODO в тех функциях, в которых необходимо действие автооизованного пользователя добавляй следующий декаратор
# (он автоматически в current_user добавляет все данные авторизованного пользователя
# TODO Новое! надо чтобы на эту страницу не мог зайти уже авторизованный
def login():
    if request.method == 'POST':
        Login.Login(request.form)
    return render_template("login.html")


@app.route('/moder')  # TODO продумать как была так, чтобы входить мог только модер и сделать страницу.
                      # TODO Изменено (Перенесено на следующие версии)
def loginM():
    return render_template("")


@app.route('/stat/<int:id>')  # TODO проблема в принятии. Нужно, чтобы передавался id в функцию и данные переходили в
                              # TODO в stat.html
def stat(id):
    data = poisk_st(id)
    return render_template("stat.html", nazv=data[1], text=data[2])


@app.route('/')
def index():
    # TODO перенаправление на /hub должно происходить
    return redirect("/hub")


def main():
    db_session.global_init("DataBase.sqlite")
    app.run()


if __name__ == '__main__':
    main()
