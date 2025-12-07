import pytest
from app import divide

def test_divide_positive_numbers():
    """Test division with two positive numbers."""
    assert divide(10, 2) == 5.0

def test_divide_negative_numbers():
    """Test division with two negative numbers."""
    assert divide(-10, -2) == 5.0

def test_divide_positive_by_negative():
    """Test division with a positive numerator and negative denominator."""
    assert divide(10, -2) == -5.0

def test_divide_negative_by_positive():
    """Test division with a negative numerator and positive denominator."""
    assert divide(-10, 2) == -5.0

def test_divide_by_one():
    """Test division by one."""
    assert divide(7, 1) == 7.0

def test_divide_zero_by_number():
    """Test division of zero by a non-zero number."""
    assert divide(0, 5) == 0.0

def test_divide_by_zero_returns_none():
    """Test division by zero should return None."""
    assert divide(10, 0) is None
    assert divide(0, 0) is None # Even 0/0 should return None as per the fix

def test_divide_float_numbers():
    """Test division with float numbers."""
    assert divide(10.5, 2.5) == 4.2

def test_divide_small_numbers():
    """Test division with very small numbers."""
    assert divide(1e-9, 1e-10) == 10.0

def test_divide_large_numbers():
    """Test division with very large numbers."""
    assert divide(1e100, 1e99) == 10.0

def test_divide_non_numeric_numerator():
    """Test division with a non-numeric numerator."""
    assert divide("abc", 2) is None

def test_divide_non_numeric_denominator():
    """Test division with a non-numeric denominator."""
    assert divide(10, "xyz") is None

def test_divide_both_non_numeric():
    """Test division with both non-numeric arguments."""
    assert divide("abc", "xyz") is None
