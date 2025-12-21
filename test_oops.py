import pytest
from oops import calculate_risk, _perform_risk_calculation
import logging

# Ensure logging is reset for each test to avoid interference
@pytest.fixture(autouse=True)
def reset_logging_config():
    # This ensures that basicConfig is not called multiple times
    # and that caplog can capture logs cleanly.
    # For this specific problem, oops.py calls basicConfig directly.
    # If it were a library, we'd configure logging in tests.
    # Since oops.py *is* the application, we just let it configure once.
    pass

def test_calculate_risk_logs_info_on_start_and_success(caplog):
    """
    Verify that calculate_risk logs INFO messages at the start and on successful completion.
    """
    with caplog.at_level(logging.INFO):
        result = calculate_risk(10)
        assert result == 12.5
        assert "Attempting to calculate risk for data: 10" in caplog.text
        assert "Successfully calculated risk: 12.5 for data: 10" in caplog.text
        assert caplog.records[0].levelname == "INFO"
        assert caplog.records[1].levelname == "INFO"

def test_calculate_risk_valid_integer_input():
    """
    Test calculate_risk with valid positive integer input.
    """
    assert calculate_risk(10) == 12.5
    assert calculate_risk(0) == 5.0

def test_calculate_risk_valid_float_input():
    """
    Test calculate_risk with valid float input.
    """
    assert calculate_risk(5.5) == (5.5 * 0.75) + 5.0
    assert calculate_risk(100.0) == 80.0

def test_calculate_risk_raises_type_error_for_non_numeric_input(caplog):
    """
    Test that calculate_risk raises TypeError for non-numeric input
    and logs an ERROR message.
    """
    with caplog.at_level(logging.ERROR):
        with pytest.raises(TypeError, match=r"Input data must be a number \(int or float\)."):
            calculate_risk("abc")
        assert "Invalid data type provided: <class 'str'>. Expected int or float." in caplog.text
        assert caplog.records[0].levelname == "ERROR"

    caplog.clear()
    with caplog.at_level(logging.ERROR):
        with pytest.raises(TypeError, match=r"Input data must be a number \(int or float\)."):
            calculate_risk([1, 2])
        assert "Invalid data type provided: <class 'list'>. Expected int or float." in caplog.text
        assert caplog.records[0].levelname == "ERROR"

def test_calculate_risk_raises_value_error_for_negative_input(caplog):
    """
    Test that calculate_risk raises ValueError for negative input
    and logs a WARNING message.
    """
    with caplog.at_level(logging.WARNING):
        with pytest.raises(ValueError, match=r"Input data must be a non-negative number."):
            calculate_risk(-5)
        assert "Negative data provided: -5. Risk calculation might be unexpected." in caplog.text
        assert caplog.records[0].levelname == "WARNING"

    caplog.clear()
    with caplog.at_level(logging.WARNING):
        with pytest.raises(ValueError, match=r"Input data must be a non-negative number."):
            calculate_risk(-0.001)
        assert "Negative data provided: -0.001. Risk calculation might be unexpected." in caplog.text
        assert caplog.records[0].levelname == "WARNING"

def test_calculate_risk_handles_unexpected_calculation_error(caplog, monkeypatch):
    """
    Test that calculate_risk logs an exception and re-raises it
    if an unexpected error occurs during the internal calculation.
    This verifies the `except Exception as e:` block.
    """
    # Monkeypatch the internal helper function to raise an error
    def mock_perform_risk_calculation(data):
        if data == 99:
            raise ZeroDivisionError("Simulated calculation error during _perform_risk_calculation")
        return (data * 0.75) + 5.0

    monkeypatch.setattr('oops._perform_risk_calculation', mock_perform_risk_calculation)

    with caplog.at_level(logging.ERROR):
        with pytest.raises(ZeroDivisionError, match=r"Simulated calculation error during _perform_risk_calculation"):
            calculate_risk(99) # Call with valid data, but the internal calculation will fail

        assert "An unexpected error occurred during risk calculation for data: 99" in caplog.text
        assert "Simulated calculation error during _perform_risk_calculation" in caplog.text
        # Check that the log record itself is an ERROR level and contains exception info
        assert caplog.records[0].levelname == "ERROR"
        assert "ZeroDivisionError" in caplog.records[0].exc_info[0].__name__
        assert "Simulated calculation error during _perform_risk_calculation" in str(caplog.records[0].exc_info[1])
