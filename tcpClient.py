import socket

# Server configuration
HOST = '127.0.0.1'  # Server's hostname or IP address
PORT = 65432        # Port to connect to

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))  # Connect to the server
    print(f"Connected to server at {HOST}:{PORT}")

    while True:
        # Send a message to the server
        message = input("You: ")
        client_socket.sendall(message.encode('utf-8'))

        # Receive response from the server
        data = client_socket.recv(1024)
        if not data:
            print("Server disconnected.")
            break
        print(f"Server: {data.decode('utf-8')}")