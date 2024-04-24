import sqlite3


def new_stat(Name, text, Login, password):
    connection = sqlite3.connect('database.sqlite')
    cursor = connection.cursor()
    data = cursor.execute(f"SELECT * FROM Pols WHERE Login={Login}")
    connection.close()
    if not data:
        if data[2]:
            cursor.execute('INSERT INTO Pols (Login, Password) VALUES (?, ?)', (Login, password))
            connection.close()
            return 'Вы успешно зарегистрировались!', 1
        else:
            connection.close()
            return 'Вы не указали пароль!', 0
    else:
        connection.close()
        return 'Данное имя пользователя занято, попробуйте другое', 0