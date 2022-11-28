import socket
import multiprocessing
import time
import os


LOCAL_IP = "localhost"
LOCAL_PORT = 20003
BUFFER_SIZE = 1024


def handle_client(server_sock):
    while True:
        try:
            connection, client_address = server_sock.accept()
            print(f"Connection from: {client_address}")
            print(f"[process-{os.getpid()}] Starting with client: {client_address}")

            time.sleep(10)

            data = connection.recv(BUFFER_SIZE)
            print(f"[process-{os.getpid()}] Received: {repr(data)}")

            connection.sendall(data.upper())
            print(f"[process-{os.getpid()}] Sent data back to the client.")

            connection.close()
            print(f"[process-{os.getpid()}] Ending.")
        except KeyboardInterrupt:
            print(f"[process-{os.getpid()}] Stopped.")


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((LOCAL_IP, LOCAL_PORT))
    sock.listen(5)

    print(f"Starting up on {LOCAL_IP} port {LOCAL_PORT}.")
    print("Waiting for a connection...")

    processes = []
    try:
        processes = [
            multiprocessing.Process(target=handle_client, args=(sock,))
            for i in range(5)
        ]

        for process in processes:
            process.start()

        for process in processes:
            process.join()
    except KeyboardInterrupt:
        print("Server stopped.")
    finally:
        if sock:
            sock.close()
        for process in processes:
            process.terminate()
