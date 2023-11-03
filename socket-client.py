from socket import *

serverIP = input('Insert server IP: ')
serverPort = input('Insert server port: ')
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP, int(serverPort)))
print('Connected to server.')
while True:
    message = input('Insert a message to be sent to server: ')
    clientSocket.send(message.encode())
    if message.upper() == "QUIT":
        print("Client informing the server that it is quitting.")
        while True:
            message = clientSocket.recv(1024).decode()
            if message.upper() == 'QUIT':
                clientSocket.close()
                exit()
            print(message)
            returned = 'Message Received.'
            clientSocket.send(returned.encode())
    print('Client has sent the message: ', message)
