import pickle
import base64

def load_session_data(token):
    """Loads analytics session from a cookie."""
    try:
        decoded_data = base64.b64decode(token)
        
        # VULNERABILITY: Insecure Deserialization
        # pickle.loads() can execute arbitrary code if the token is malicious.
        # An attacker can serialize a payload that runs 'cat /etc/passwd'
        session_obj = pickle.loads(decoded_data)
        
        return session_obj
    except Exception as e:
        print(f"Error loading session: {e}")
        return {}
