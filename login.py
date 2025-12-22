import sqlite3

def login(username, password):
    # VULNERABILITY: Raw f-string used in SQL query
    # A user can enter: " admin' -- " to bypass the password
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return "Login Successful"
    else:
        return "Access Denied"
