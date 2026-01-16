import json
import base64

def load_session(token):
    data = base64.b64decode(token)
    try:
        return json.loads(data.decode())
    except json.JSONDecodeError:
        raise ValueError("Invalid session token")