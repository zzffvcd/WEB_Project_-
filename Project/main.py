from data import db_session
from flask import Flask, render_template, redirect
from forms.user import RegisterForm
from flask_login import LoginManager, current_user, login_required, logout_user, login_user
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


def poisk_statbi():
    conn = sqlite3.connect('database.sqlite')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, url_image, text, idpols FROM statbi")
    rows = cursor.fetchall()
    for row in rows:
        data = {
            'id': row[0],
            'name': row[1],
            'url_image': row[2],
            'text': row[3],
            'idpols': row[4]
        }
    conn.close()
    if data['url_image']:
        return [data['id'], data['name'], data['url_image'], data['text'], data['idpols'], 0]
    else:
        return [data['id'], data['name'], data['text'], data['idpols'], 1]


@app.route("/main")
def mainn():
    data = poisk_statbi()
    return render_template("templates/base.html", menu=data)


@app.route('/register')
def register():
    return render_template("templates/register.html")



@app.route('/login')
def login():
    return render_template("templates/login.html")


@app.route('/moder') #TODO продумать как была так, чтобы входить мог только модер и сделать страницу
def login():
    return render_template("")


@app.route('/stat') #TODO страница со статьёй
def login():
    return render_template("")


def main():
    db_session.global_init("DataBase.sqlite")
    app.run()


if __name__ == '__main__':
    main()