import sqlite3


def Login(Login, passwod):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    data = cursor.execute(f"SELECT * FROM Pols WHERE Login={Login}")
    if data:
        if data[2] == passwod:
            connection.close()
            return 'Вход!'
        else:
            connection.close()
            return 'Указан неправильный пароль или электронная почта!'
    else:
        connection.close()
        return 'Указан неправильный пароль или электронная почта!'
