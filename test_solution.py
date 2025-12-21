import pytest
from app import calculate_expression

def test_basic_addition():
    assert calculate_expression("2 + 3") == 5.0
    assert calculate_expression("2.5 + 3.5") == 6.0
    assert calculate_expression("2 + 3.5") == 5.5

def test_basic_subtraction():
    assert calculate_expression("5 - 2") == 3.0
    assert calculate_expression("5.5 - 2.5") == 3.0
    assert calculate_expression("5 - 2.5") == 2.5

def test_basic_multiplication():
    assert calculate_expression("2 * 3") == 6.0
    assert calculate_expression("2.5 * 2") == 5.0
    assert calculate_expression("2.5 * 3.0") == 7.5

def test_basic_division():
    assert calculate_expression("6 / 2") == 3.0
    assert calculate_expression("7 / 2") == 3.5
    assert calculate_expression("7.0 / 2.0") == 3.5
    assert calculate_expression("10 / 4") == 2.5

def test_order_of_operations():
    assert calculate_expression("2 + 3 * 4") == 14.0
    assert calculate_expression("(2 + 3) * 4") == 20.0
    assert calculate_expression("10 - 4 / 2") == 8.0
    assert calculate_expression("10 / 2 + 3") == 8.0

def test_unary_minus():
    assert calculate_expression("-5") == -5.0
    assert calculate_expression("10 + -5") == 5.0
    assert calculate_expression("-(2 + 3)") == -5.0
    assert calculate_expression("5 * -2") == -10.0

def test_complex_expressions():
    assert calculate_expression("(10 + 20) * (3 - 1) / 5") == 12.0
    assert calculate_expression("1 + 2 * 3 - 4 / 2 + (5 - 1)") == 9.0

def test_zero_division_error():
    with pytest.raises(ValueError):
        calculate_expression("1 / 0")
    with pytest.raises(ValueError):
        calculate_expression("(5 - 5) / 0")
    with pytest.raises(ValueError):
        calculate_expression("10 / (2 - 2)")

def test_invalid_syntax():
    with pytest.raises(ValueError):
        calculate_expression("1 +")
    with pytest.raises(ValueError):
        calculate_expression("(1 + 2")
    with pytest.raises(ValueError):
        calculate_expression("1 + * 2")
    with pytest.raises(ValueError):
        calculate_expression("(")

def test_unsupported_operators():
    with pytest.raises(ValueError):
        calculate_expression("1 ** 2") # Power operator
    with pytest.raises(ValueError):
        calculate_expression("1 % 2")  # Modulo operator
    with pytest.raises(ValueError):
        calculate_expression("1 // 2") # Floor division

def test_unsupported_functions_or_names():
    with pytest.raises(ValueError):
        calculate_expression("abs(-5)")
    with pytest.raises(ValueError):
        calculate_expression("sin(30)")
    with pytest.raises(ValueError):
        calculate_expression("my_var + 1")
    with pytest.raises(ValueError):
        calculate_expression("1 + []")
    with pytest.raises(ValueError):
        calculate_expression("1 + {}")

def test_non_numeric_input():
    with pytest.raises(ValueError):
        calculate_expression("hello")
    with pytest.raises(ValueError):
        calculate_expression("1 + abc")
    with pytest.raises(ValueError):
        calculate_expression("true + false")

def test_empty_string():
    with pytest.raises(ValueError):
        calculate_expression("")
    with pytest.raises(ValueError):
        calculate_expression("   ")

def test_none_input():
    with pytest.raises(ValueError):
        calculate_expression(None)

def test_non_string_input():
    with pytest.raises(ValueError):
        calculate_expression(123)
    with pytest.raises(ValueError):
        calculate_expression([1, 2])
