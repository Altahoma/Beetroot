import socket


server_ip = "localhost"
server_port = 20001
buffer_size = 1024
msg_from_client = 'Hello UDP Server'
bytes_to_send = str.encode(msg_from_client)

udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_client_socket.sendto(bytes_to_send, (server_ip, server_port))

msg_from_server = udp_client_socket.recvfrom(buffer_size)
msg = f'Message from server: {msg_from_server[0]}'
print(msg)
