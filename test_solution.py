import pytest
from app import verify_admin

def test_verify_admin_correct_password():
    """Test that verify_admin returns True for the correct password."""
    assert verify_admin("admin_secret_123") is True

def test_verify_admin_incorrect_password():
    """Test that verify_admin returns False for an incorrect password."""
    assert verify_admin("wrong_password") is False

def test_verify_admin_empty_password():
    """Test that verify_admin returns False for an empty password."""
    assert verify_admin("") is False

def test_verify_admin_different_case_password():
    """Test that verify_admin returns False for a password with different casing."""
    assert verify_admin("Admin_secret_123") is False

def test_verify_admin_password_with_extra_chars():
    """Test that verify_admin returns False for a password with extra characters."""
    assert verify_admin("admin_secret_123 ") is False
