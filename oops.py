import logging
import sys

# Configure logging to capture output for tests and general use.
# By default, logs to stderr, which pytest's caplog fixture can capture.
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)

def _perform_risk_calculation(data):
    """Internal helper for the actual risk calculation logic."""
    # This is where the core logic resides. It's separated to allow
    # easier testing of the outer try-except block for unexpected errors.
    return (data * 0.75) + 5.0

def calculate_risk(data):
    """
    Calculates a risk score based on the input data.
    
    - Logs the input data at INFO level.
    - Raises TypeError if data is not a number.
    - Raises ValueError if data is a negative number.
    - Logs and re-raises any unexpected errors during the calculation.
    
    Args:
        data (int or float): The input data for risk calculation.
        
    Returns:
        float: The calculated risk score.
        
    Raises:
        TypeError: If `data` is not an int or float.
        ValueError: If `data` is a negative number.
        Exception: For any other unexpected errors during calculation.
    """
    logging.info(f"Attempting to calculate risk for data: {data}")

    if not isinstance(data, (int, float)):
        logging.error(f"Invalid data type provided: {type(data)}. Expected int or float.")
        raise TypeError("Input data must be a number (int or float).")

    if data < 0:
        logging.warning(f"Negative data provided: {data}. Risk calculation might be unexpected.")
        raise ValueError("Input data must be a non-negative number.")

    try:
        risk = _perform_risk_calculation(data)
        logging.info(f"Successfully calculated risk: {risk} for data: {data}")
        return risk
    except Exception as e:
        # This block catches any unexpected errors during the _perform_risk_calculation.
        # It logs the exception details and re-raises the original exception,
        # preventing silent failures (which a bare 'except' would cause).
        logging.exception(f"An unexpected error occurred during risk calculation for data: {data}")
        raise # Re-raise the original exception
