import os

STRIPE_API_KEY = os.getenv("STRIPE_API_KEY", "")
AWS_SECRET = os.getenv("AWS_SECRET", "")

def get_config():
    return {"key": STRIPE_API_KEY}