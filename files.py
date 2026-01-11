def read_user_file(filename):
    # VULNERABILITY: No check for "../"
    with open("/var/www/uploads/" + filename, 'r') as f:
        return f.read()
