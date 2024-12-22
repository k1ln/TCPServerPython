import socket

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

# Create a TCP/IP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))  # Bind the socket to the address and port
    server_socket.listen()            # Listen for incoming connections
    print(f"Server listening on {HOST}:{PORT}")

    # Wait for a connection
    conn, addr = server_socket.accept()  # Accept a client connection
    with conn:
        print(f"Connected by {addr}")
        while True:
            # Receive data from the client
            data = conn.recv(1024)
            if not data:
                print("Client disconnected.")
                break
            print(f"Client: {data.decode('utf-8')}")

            # Send a message to the client
            message = input("You: ")
            conn.sendall(message.encode('utf-8'))