import os

UPLOAD_DIR = "/var/www/uploads"

def read_user_document(filename):
    """Reads a document uploaded by the user."""
    
    # VULNERABILITY: Path Traversal
    # No validation if filename contains "../"
    # Attack: filename = "../../etc/passwd"
    file_path = os.path.join(UPLOAD_DIR, filename)
    
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"

def save_avatar(user_id, image_data):
    # VULNERABILITY: Unrestricted File Upload (No check for .exe or .php)
    with open(f"avatars/{user_id}.jpg", "wb") as f:
        f.write(image_data)
