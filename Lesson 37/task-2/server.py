import socket
import threading
import time


LOCAL_IP = "localhost"
LOCAL_PORT = 20001
BUFFER_SIZE = 1024


def handle_client(conn, addr):
    print(f"[thread-{addr[1]}] Starting with client: {addr}")

    time.sleep(10)

    data = conn.recv(BUFFER_SIZE)
    print(f"[thread-{addr[1]}] Received: {repr(data)}")

    conn.sendall(data.upper())
    print(f"[thread-{addr[1]}] Sent data back to the client.")

    conn.close()
    print(f"[thread-{addr[1]}] Ending.")


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((LOCAL_IP, LOCAL_PORT))
sock.listen(1)

print(f"Starting up on {LOCAL_IP} port {LOCAL_PORT}.")

all_threads = []
try:
    while True:
        print("Waiting for a connection...")
        connection, client_address = sock.accept()

        print(f"Connection from: {client_address}")

        t = threading.Thread(target=handle_client, args=(connection, client_address))
        t.start()

        all_threads.append(t)
except KeyboardInterrupt:
    print("Server stopped.")
finally:
    if sock:
        sock.close()
    for t in all_threads:
        t.join()
