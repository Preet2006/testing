import psycopg2
import re

def login(username, password):
    try:
        # Validate input
        if not re.match('^[a-zA-Z0-9]{1,50}$', username) or not re.match('^[a-zA-Z0-9]{1,50}$', password):
            raise ValueError('Invalid username or password')
        # Connect to database
        conn = psycopg2.connect(
            host='localhost',
            database='mydatabase',
            user='myuser',
            password='mypassword'
        )
        # Create a cursor object
        cur = conn.cursor()
        # Use parameterized query
        cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        # Fetch results
        results = cur.fetchall()
        # Close the cursor and connection
        cur.close()
        conn.close()
        # Return True if user exists, False otherwise
        return len(results) > 0
    except psycopg2.Error as e:
        raise ValueError('Database error: ' + str(e))
