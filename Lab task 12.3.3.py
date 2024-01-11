def read_data_from_file(filename):
    """Reads data from a file and handles the file not found error."""
    try:
        with open(filename, "r") as file:
            data = file.read()
            print(data)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Example usage:
read_data_from_file("my_data.txt")