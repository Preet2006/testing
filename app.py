import sqlite3
import os
import subprocess

def setup_database():
    """Helper to create a dummy database so tests don't fail immediately."""
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)')
    c.execute("INSERT INTO users VALUES ('admin', 'secret123')")
    c.execute("INSERT INTO users VALUES ('user', 'password')")
    conn.commit()
    conn.close()

# VULNERABILITY 1: SQL Injection
# The Red Team should be able to bypass login using: ' OR '1'='1
def login(username, password):
    # Ensure DB exists
    if not os.path.exists('users.db'):
        setup_database()
        
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # CRITICAL SECURITY FLAW: F-String usage in SQL
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"[DEBUG] Executing: {query}")
    
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    
    if user:
        return True
    return False

# VULNERABILITY 2: Command Injection
# The Red Team should be able to run other commands using: 8.8.8.8; whoami
def ping_address(ip_address):
    # CRITICAL SECURITY FLAW: Using os.system with unsanitized input
    command = f"ping -c 1 {ip_address}"
    print(f"[DEBUG] Running: {command}")
    
    # This executes whatever string is passed, including malicious commands
    return os.system(command)

# VULNERABILITY 3: Unsafe Eval
# The Red Team can execute python code like: __import__('os').system('ls')
def calculate_price(expression):
    # CRITICAL SECURITY FLAW: Using eval() on user input
    print(f"[DEBUG] Calculating: {expression}")
    return eval(expression)
