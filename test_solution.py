import logging
from app import process_data

def test_process_data_negative_value_logs_error(caplog):
    """Test that a negative value logs an ERROR and returns False."""
    # Set caplog level to capture ERROR messages
    caplog.set_level(logging.ERROR)
    
    result = process_data(-5)
    
    assert not result
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "ERROR"
    assert "Data processing failed: Value -5 is negative." in caplog.text

def test_process_data_invalid_type_logs_error(caplog):
    """Test that an invalid type logs an ERROR and returns False."""
    caplog.set_level(logging.ERROR)
    
    result = process_data("abc")
    
    assert not result
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "ERROR"
    assert "Invalid input type: <class 'str'>. Expected int or float." in caplog.text

def test_process_data_positive_value_logs_info(caplog):
    """Test that a positive value logs INFO and returns True."""
    # Set caplog level to capture INFO messages
    caplog.set_level(logging.INFO)
    
    result = process_data(10)
    
    assert result
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "INFO"
    assert "Successfully processed data with value: 10" in caplog.text
    # Ensure no ERROR logs were generated
    assert not any(r.levelname == "ERROR" for r in caplog.records)

def test_process_data_zero_value_logs_info(caplog):
    """Test that a zero value logs INFO and returns True."""
    caplog.set_level(logging.INFO)
    
    result = process_data(0)
    
    assert result
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "INFO"
    assert "Successfully processed data with value: 0" in caplog.text

def test_process_data_float_value_logs_info(caplog):
    """Test that a float value logs INFO and returns True."""
    caplog.set_level(logging.INFO)
    
    result = process_data(3.14)
    
    assert result
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "INFO"
    assert "Successfully processed data with value: 3.14" in caplog.text
