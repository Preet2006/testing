import pytest
from app import calculate_ratio

def test_calculate_ratio_normal_operation():
    """Test that the function returns the correct ratio for valid inputs."""
    assert calculate_ratio(10, 2) == 5.0
    assert calculate_ratio(7, 3) == pytest.approx(2.333333)
    assert calculate_ratio(0, 5) == 0.0

def test_calculate_ratio_zero_division_error():
    """Test that ZeroDivisionError is caught and handled correctly."""
    assert calculate_ratio(10, 0) == "Error: Cannot divide by zero."
    assert calculate_ratio(0, 0) == "Error: Cannot divide by zero."

def test_calculate_ratio_type_error_propagates():
    """Test that a TypeError (or other non-ZeroDivisionError) propagates."""
    with pytest.raises(TypeError):
        calculate_ratio(10, "a")
    with pytest.raises(TypeError):
        calculate_ratio("b", 2)

def test_calculate_ratio_float_inputs():
    """Test with float inputs."""
    assert calculate_ratio(10.0, 2.5) == 4.0
    assert calculate_ratio(5.5, 2.0) == 2.75
