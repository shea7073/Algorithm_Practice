from socket import *

server_port = 14000
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('', server_port))

server_socket.listen(1)

print('The server is ready!')

while True:
    connection_socket, addr = server_socket.accept()
    message = connection_socket.recv(2048)
    print(message.decode())
    modified_message = message.decode().upper()
    connection_socket.send(modified_message.encode())
    print(modified_message)
    connection_socket.close()
    print('connection socket is closed')