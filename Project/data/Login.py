import sqlite3


def register(Login, passwod):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    data = cursor.execute(f"SELECT * FROM Pols WHERE Login={Login}")
    connection.close()
    if data:
        if data[2] == passwod:
            return 'Вход!'
        else:
            return 'Указан неправильный пароль или электронная почта!'
    else:
        return 'Указан неправильный пароль или электронная почта!'
