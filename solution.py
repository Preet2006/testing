def verify_admin(password: str) -> bool:
    """
    Verifies if the provided password matches the admin secret.

    Args:
        password: The password string to check.

    Returns:
        True if the password matches 'admin_secret_123', False otherwise.
    """
    ADMIN_SECRET_PASSWORD = "admin_secret_123"
    return password == ADMIN_SECRET_PASSWORD
