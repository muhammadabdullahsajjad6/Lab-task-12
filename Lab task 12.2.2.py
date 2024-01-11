import socket

def connect_to_server(server_address, port):
    """Attempts to connect to a server and handles potential network errors."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((server_address, port))
            print("Connected to server!")
    except socket.error as e:
        print(f"Error connecting to server: {e}")

# Example usage:
connect_to_server("example.com", 80)