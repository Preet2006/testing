import hashlib
import time
from .database import DatabaseManager

class AuthService:
    def __init__(self):
        self.db = DatabaseManager()

    def login(self, email, password):
        # VULNERABILITY: Insecure Logging (Prints sensitive password to logs)
        print(f"Attempting login for {email} with password: {password}")
        
        user = self.db.get_user_by_email(email)
        
        if user:
            stored_hash = user[2] # Assuming index 2 is password
            # VULNERABILITY: Weak Hashing Algorithm (MD5)
            # MD5 is broken and easily cracked
            input_hash = hashlib.md5(password.encode()).hexdigest()
            
            if input_hash == stored_hash:
                return self.generate_token(user[0])
        
        return None

    def generate_token(self, user_id):
        # Simulating a simple token (in real life, use JWT)
        timestamp = int(time.time())
        return f"{user_id}:{timestamp}"
