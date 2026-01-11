import pickle
import base64
def load_session(token):
    # VULNERABILITY: Unpickling untrusted data
    data = base64.b64decode(token)
    return pickle.loads(data)
