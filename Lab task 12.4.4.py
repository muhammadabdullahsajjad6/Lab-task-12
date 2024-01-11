class InvalidInputError(Exception):
    """Raised when invalid input is encountered."""
    pass

def process_data(value):
    """Raises InvalidInputError if the value is negative."""
    if value < 0:
        raise InvalidInputError("Value cannot be negative.")
    else:
        print("Processing value:", value)

# Example usage:
try:
    process_data(-5)  # This will raise the custom exception
except InvalidInputError as e:
    print("Error:", e)