import sqlite3

def get_user_details():
    user_id = input("Enter User ID: ")
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # VULNERABLE: String formatting for SQL queries
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    
    cursor.execute(query)
    print(cursor.fetchone())

if __name__ == "__main__":
    get_user_details()
