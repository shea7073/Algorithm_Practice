# Sean  Shea
from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
server_port = 7073
serverSocket.bind(('', server_port))
serverSocket.listen(1)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(2048)
        filename = message.split()[1]
        f = open(filename)
        outputdata = f.read()
        connectionSocket.send('HTTP/1.1 200 OK\r\n\r\n'.encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
        connectionSocket.close()
        serverSocket.close()
        sys.exit()