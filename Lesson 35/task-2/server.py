import socket
import pickle
from caesarcipher import CaesarCipher


local_ip = "localhost"
local_port = 20001
buffer_size = 1024

udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_server_socket.bind((local_ip, local_port))

print("UDP server up and listening")

while True:
    data, address = udp_server_socket.recvfrom(buffer_size)
    decoded_data = pickle.loads(data)

    client_code = decoded_data[0]
    client_msg = decoded_data[1]

    print(f'Message from client: {client_msg}')
    print(f'Client code: {client_code}')

    encrypted_data = CaesarCipher(message=client_msg, offset=client_code).encoded
    bytes_to_sent = str.encode(encrypted_data)
    udp_server_socket.sendto(bytes_to_sent, address)
    print(f'Sent encrypted message.')
