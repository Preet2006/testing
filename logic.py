from database import run_query_safe

def search_user(username):
    query = "SELECT * FROM users WHERE username = ?"
    return run_query_safe(query, (username,))

def login(username, password):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    return run_query_safe(query, (username, password))