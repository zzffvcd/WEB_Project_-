from data import db_session
from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, current_user, login_required, logout_user, login_user
from data import poisk_st
from data import register
from data import Login
from data import new_stat
from data.name_table import User, Statbi
from forms.nameTable import LoginForm, NewStat, RegisterForm

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


@app.route("/")
@app.route("/hub")
def hub():
    data = poisk_st.poisk_statbi()
    return render_template("hub.html", menu=data, title='Главная страница')


@app.route("/stat/<int:id>")
def stat(id):
    data = poisk_st.poisk_statbi()
    for elem in data:
        if id == elem['id']:
            return render_template("stat.html", name=elem['name'], text=elem['text'])


@app.route("/newstat")
@login_required
def newstat():
    form = NewStat()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        stat = Statbi(name=form.name.data,
                      URL_image=form.URL_image.data,
                      Text=form.Text.data
                      )
        stat.IdPols = current_user.id
        db_sess.add(stat)
        db_sess.commit()
        return redirect('/login')
    return render_template('newstat.html', title='Регистрация', menu=form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.Login == form.Login.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(Login=form.Login.data)
        user.set_password(form.Password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.Login == form.Login.data).first()
        if user and user.check_password(form.Password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/moder')  # TODO продумать как была так, чтобы входить мог только модер и сделать страницу.
# TODO Изменено (Перенесено на следующие версии)
def loginM():
    return render_template("")


def main():
    db_session.global_init("DataBase.sqlite")
    app.run()


if __name__ == '__main__':
    main()
