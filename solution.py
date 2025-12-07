import logging

# Configure logging at the module level. 
# This ensures that if the app is run directly, logs are outputted.
# For testing with pytest's caplog, caplog temporarily overrides handlers.
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def process_data(value):
    """
    Processes a given value. Logs an error if the value is invalid (negative or wrong type),
    otherwise logs an info message upon successful processing.
    """
    if not isinstance(value, (int, float)):
        # Replaced print() with logging.error()
        logging.error(f"Invalid input type: {type(value)}. Expected int or float.")
        return False
    
    if value < 0:
        # Replaced print() with logging.error()
        logging.error(f"Data processing failed: Value {value} is negative.")
        return False
    else:
        # Original print() might have been here, now replaced with logging.info()
        logging.info(f"Successfully processed data with value: {value}")
        # Simulate some actual data processing here
        return True

if __name__ == '__main__':
    print("--- Testing process_data with various inputs ---")
    print("\nProcessing 10:")
    process_data(10)

    print("\nProcessing -5:")
    process_data(-5)

    print("\nProcessing 'hello':")
    process_data("hello")

    print("\nProcessing 0:")
    process_data(0)

    print("\nProcessing 3.14:")
    process_data(3.14)
    print("------------------------------------------------")
