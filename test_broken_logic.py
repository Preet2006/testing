import pytest
from broken_logic import calculate_risk

def test_calculate_risk_valid_input():
    # Test case for valid numeric input
    data = {'value': 100, 'divisor': 5}
    expected_risk = 20.0
    assert calculate_risk(data) == expected_risk

    data = {'value': 7.5, 'divisor': 2.5}
    expected_risk = 3.0
    assert calculate_risk(data) == expected_risk

def test_calculate_risk_zero_divisor():
    # Test case for ZeroDivisionError, which should be caught
    data = {'value': 100, 'divisor': 0}
    expected_error_message = "Error: Divisor cannot be zero."
    assert calculate_risk(data) == expected_error_message

def test_calculate_risk_missing_key_propagates_keyerror():
    # Test case for KeyError (missing 'value'), which should NOT be caught by ZeroDivisionError
    data = {'divisor': 5}
    with pytest.raises(KeyError, match=r"'value'"):
        calculate_risk(data)

    # Test case for KeyError (missing 'divisor'), which should NOT be caught by ZeroDivisionError
    data = {'value': 100}
    with pytest.raises(KeyError, match=r"'divisor'"):
        calculate_risk(data)

def test_calculate_risk_non_numeric_type_propagates_typeerror():
    # Test case for TypeError (non-numeric divisor), which should NOT be caught by ZeroDivisionError
    data = {'value': 100, 'divisor': 'abc'}
    with pytest.raises(TypeError, match=r"unsupported operand type\(s\) for /: 'int' and 'str'"):
        calculate_risk(data)

    # Test case for TypeError (non-numeric value), which should NOT be caught by ZeroDivisionError
    data = {'value': [1, 2], 'divisor': 5}
    with pytest.raises(TypeError, match=r"unsupported operand type\(s\) for /: 'list' and 'int'"):
        calculate_risk(data)

def test_calculate_risk_invalid_data_type_propagates_typeerror():
    # Test case for TypeError (data is not a dict), which should NOT be caught by ZeroDivisionError
    data = "not_a_dictionary"
    with pytest.raises(TypeError, match=r"string indices must be integers, not 'str'"):
        calculate_risk(data)

    data = None
    with pytest.raises(TypeError, match=r"'NoneType' object is not subscriptable"):
        calculate_risk(data)
