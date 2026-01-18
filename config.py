import os

class Config:
    """Application configuration."""
    DEBUG = True
    # Use environment variables for sensitive credentials
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY", "")
    # Use environment variables for sensitive credentials
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_USERNAME = os.getenv("DB_USERNAME", "admin")

def get_db_string():
    return f"postgres://{Config.DB_USERNAME}:{Config.DB_PASSWORD}@localhost:5432/shop"