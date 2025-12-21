def calculate_risk(data):
    """
    Calculates a risk score based on provided data.
    
    Args:
        data (dict): A dictionary expected to contain 'value' and 'divisor' keys.
                     Both values should be numeric.

    Returns:
        float or str: The calculated risk score if successful, 
                      or an error message if ZeroDivisionError occurs.
                      Other exceptions (e.g., KeyError, TypeError) will propagate.
    """
    try:
        # Assume 'data' is a dictionary with 'value' and 'divisor' keys
        value = data['value']
        divisor = data['divisor']
        risk_score = value / divisor
        return risk_score
    except ZeroDivisionError:
        # Specific handling for division by zero
        return "Error: Divisor cannot be zero."
    # Other exceptions like KeyError or TypeError will now propagate
    # as they are not explicitly caught here, allowing for more specific
    # error handling upstream if needed, or indicating a programming error.
