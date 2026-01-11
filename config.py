# VULNERABILITY: API Key exposed in code
STRIPE_API_KEY = "sk_live_51Mz..."
AWS_SECRET = "AKIAIOSFODNN7EXAMPLE"
def get_config():
    return {"key": STRIPE_API_KEY}
