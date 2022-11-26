import socket


local_ip = "localhost"
local_port = 20001
buffer_size = 1024
msg_from_server = "Hello UDP Client"
bytes_to_send = str.encode(msg_from_server)

udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_server_socket.bind((local_ip, local_port))

print("UDP server up and listening")

while True:
    data, address = udp_server_socket.recvfrom(buffer_size)

    client_msg = f"Message from client: {data}"
    client_ip = f"Client IP Address: {address}"

    print(client_msg)
    print(client_ip)

    udp_server_socket.sendto(bytes_to_send, address)
