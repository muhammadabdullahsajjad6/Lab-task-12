def validate_parameter(value, min_value, max_value):
    """Raises an AssertionError if the value is not within the specified range."""
    assert min_value <= value <= max_value, f"Value {value} is not within the valid range ({min_value}-{max_value})"
    return value

# Example usage:
try:
    result = validate_parameter(5, 1, 10)  # This will succeed
except AssertionError as e:
    print("Error:", e)