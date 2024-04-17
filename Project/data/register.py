import sqlite3


def register(Login, password):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    data = cursor.execute(f"SELECT * FROM Pols WHERE Login={Login}")
    connection.close()
    if not data:
        if data[2]:
            return 'Вы успешно зарегистрировались!'
        else:
            return 'Вы не указали пароль!'
        #TODO добавить данные в таблицу
    else:
        return 'Данное имя пользователя занято, попробуйте другое'
