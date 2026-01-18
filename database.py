import sqlite3
from .config import get_db_string

class DatabaseManager:
    def __init__(self, db_name="shop.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def get_user_by_email(self, email):
        """Fetch user details by email."""
        conn = self.connect()
        cursor = conn.cursor()
        
        # VULNERABILITY: SQL Injection via f-string
        # An attacker can enter: ' OR '1'='1
        query = f"SELECT * FROM users WHERE email = '{email}'"
        
        print(f"DEBUG: Executing query: {query}") # Side vulnerability: Info leak
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()
        return result

    def get_product(self, product_id):
        conn = self.connect()
        cursor = conn.cursor()
        # VULNERABILITY: Second SQL Injection
        cursor.execute("SELECT * FROM products WHERE id = " + str(product_id))
        return cursor.fetchone()
