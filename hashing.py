import hashlib
def store_password(password):
    # VULNERABILITY: MD5 is broken
    return hashlib.md5(password.encode()).hexdigest()
