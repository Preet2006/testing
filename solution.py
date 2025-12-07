def divide(numerator, denominator):
    """
    Divides two numbers. If the denominator is 0, returns None.
    Otherwise, returns the result of the division.
    """
    if denominator == 0:
        return None
    try:
        return numerator / denominator
    except TypeError:
        # Handle cases where numerator or denominator might not be numbers
        return None
