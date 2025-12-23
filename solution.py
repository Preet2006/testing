import sqlite3

def login(user, pass_):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (user, pass_))
    result = cursor.fetchone()
    conn.close()
    return result is not None