from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Please enter a lowercase string: ")

clientSocket.sendto(message.encode(), (serverName, serverPort))

modified_message, server_address = clientSocket.recvfrom(2048)

print(modified_message.decode())







