import pickle
import sys
import base64
import json

def load_user_profile(data_string):
    print("Loading user profile...")
    try:
        # Simulate receiving a token from a web cookie
        decoded = base64.b64decode(data_string)
        
        # VULNERABILITY: Insecure Deserialization
        # pickle.loads() executes code immediately upon loading.
        # Red Team will inject a payload that prints "EXPLOIT_SUCCESS"
        user_obj = pickle.loads(decoded)
        
        print(f"User loaded: {user_obj}")
    except Exception as e:
        print(f"Error loading profile: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        load_user_profile(sys.argv[1])
    else:
        print("Usage: python user_loader.py <base64_string>")
