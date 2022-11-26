import socket
import pickle


server_ip = "localhost"
server_port = 20001
buffer_size = 1024
msg_from_client = 'Hello UDP Server'
caesar_code = 7
bytes_to_sent = pickle.dumps([caesar_code, msg_from_client])

udp_client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_client_socket.sendto(bytes_to_sent, (server_ip, server_port))
msg_from_server = udp_client_socket.recvfrom(buffer_size)

msg = f'Message from server: {msg_from_server[0]}'
print(msg)
