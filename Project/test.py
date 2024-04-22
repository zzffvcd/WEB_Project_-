from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, current_user, login_required, logout_user, login_user
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/register', methods=['POST', 'GET'])
def regster():
    if request.method == 'POST':
        print(request.form)
    return render_template("templates/register.html")


def main():
    app.run()


if __name__ == '__main__':
    main()
