import sqlite3

def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE user = ? AND pass = ?"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.close()
    return result