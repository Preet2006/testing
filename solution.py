def calculate_ratio(numerator, denominator):
    """
    Calculates the ratio of two numbers.
    Handles ZeroDivisionError specifically.
    
    Args:
        numerator (int or float): The dividend.
        denominator (int or float): The divisor.
        
    Returns:
        float or str: The calculated ratio, or an error message if division by zero occurs.
                      Other exceptions will propagate.
    """
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    # Note: Other exceptions like TypeError will now propagate
    # if not caught by a more general handler further up the call stack.
