import sqlite3

def get_connection():
    return sqlite3.connect('users.db')

def run_query_unsafe(sql_query):
    """
    Executes a raw SQL string. VULNERABLE if input is not sanitized.
    """
    conn = get_connection()
    cursor = conn.cursor()
    print(f"[DB] Executing Raw: {sql_query}")
    cursor.execute(sql_query)
    results = cursor.fetchall()
    conn.close()
    return results

def run_query_safe(sql_query, params):
    """
    Executes a parameterized query. SECURE against SQL Injection.
    """
    conn = get_connection()
    cursor = conn.cursor()
    print(f"[DB] Executing Safe: {sql_query} with {params}")
    cursor.execute(sql_query, params)
    results = cursor.fetchall()
    conn.close()
    return results
