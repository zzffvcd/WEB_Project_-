import sqlite3


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
