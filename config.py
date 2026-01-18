import os

class Config:
    """Application configuration."""
    DEBUG = True
    # VULNERABILITY: Hardcoded AWS Secret Key
    AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE_SECRET_KEY_12345"
    # VULNERABILITY: Hardcoded Database Password
    DB_PASSWORD = "production_password_do_not_share"

def get_db_string():
    return f"postgres://admin:{Config.DB_PASSWORD}@localhost:5432/shop"
