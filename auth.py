import sqlite3
def login(username, password):
    conn = sqlite3.connect('users.db')
    # VULNERABILITY: Raw SQL String Concatenation
    query = "SELECT * FROM users WHERE user = '" + username + "' AND pass = '" + password + "'"
    cursor = conn.execute(query)
    return cursor.fetchone()
