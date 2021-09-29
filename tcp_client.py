from socket import *

server_name = 'localhost'
server_port = 14000

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect((server_name, server_port))

message = input('Input lower case string: ')

client_socket.send(message.encode())

modified_message = client_socket.recv(2048)

print(modified_message.decode())

client_socket.close()