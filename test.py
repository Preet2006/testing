import sqlite3

def get_user_details():
    user_id = input("Enter User ID: ")
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE id = ?"
    cursor.execute(query, (user_id,))
    print(cursor.fetchone())

if __name__ == "__main__":
    get_user_details()