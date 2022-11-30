import socket
import asyncio


LOCAL_IP = "localhost"
LOCAL_PORT = 20004
BUFFER_SIZE = 1024


async def handle_client(conn, addr):
    loop = asyncio.get_event_loop()
    print(f"[async-{addr[1]}] Starting with client: {addr}")

    await asyncio.sleep(10)

    data = await loop.sock_recv(conn, BUFFER_SIZE)
    print(f"[async-{addr[1]}] Received: {repr(data)}")

    await loop.sock_sendall(conn, data.upper())
    print(f"[async-{addr[1]}] Sent data back to the client.")

    conn.close()
    print(f"[async-{addr[1]}] Ending.")


async def run_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((LOCAL_IP, LOCAL_PORT))
    sock.listen(1)
    sock.setblocking(False)

    print(f"Starting up on {LOCAL_IP} port {LOCAL_PORT}.")
    loop = asyncio.get_event_loop()

    try:
        while True:
            print("Waiting for a connection...")
            connection, client_address = await loop.sock_accept(sock)

            print(f"Connection from: {client_address}")
            loop.create_task(handle_client(connection, client_address))
    finally:
        if sock:
            sock.close()


if __name__ == "__main__":
    try:
        asyncio.run(run_server())
    except KeyboardInterrupt:
        print("Server stopped.")
