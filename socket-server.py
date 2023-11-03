from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverIP = gethostbyname(gethostname())
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server address: ', serverIP)
print('The server port: ', serverPort)
print('The server is ready to receive messages.')
while True:
    connectionSocket, addr = serverSocket.accept()
    print('Server is connected to client at the address: ', addr)
    log = []
    while True:
        message = connectionSocket.recv(1024).decode()
        log.append(message)
        print('Server received message: ', message)
        if message.upper() == "QUIT":
            print("Client informed server that it is quitting.")
            for message in log:
                connectionSocket.send(message.encode())
                returned = connectionSocket.recv(1024).decode() # Ensure messages are delivered in order.
            connectionSocket.close()
            exit()
