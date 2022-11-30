import socket


SERVER_IP = "localhost"
SERVER_PORT = 20004
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT))
    print("Connected to the server")

    message = b"Hello from client 1!"
    s.send(message)
    print("Sent:", message)

    data = s.recv(BUFFER_SIZE)
    print(f"Received: {repr(data)}")
