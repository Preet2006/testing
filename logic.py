import sqlite3

def run_query_safe(query, params):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchone()
    conn.close()
    return result

def search_user(username):
    query = "SELECT * FROM users WHERE name = ?"
    return run_query_safe(query, (username,))

def login(username, password):
    query = "SELECT * FROM users WHERE name = ? AND pass = ?"
    result = run_query_safe(query, (username, password))
    return result is not None