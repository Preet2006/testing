from database import run_query_unsafe

def search_user(username):
    # VULNERABILITY: Constructing SQL with f-string
    # The agent should switch this to use 'run_query_safe' from database.py
    query = f"SELECT * FROM users WHERE name = '{username}'"
    return run_query_unsafe(query)

def login(username, password):
    query = f"SELECT * FROM users WHERE name = '{username}' AND pass = '{password}'"
    return run_query_unsafe(query)
