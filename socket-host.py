import signal
import socket
import threading
import os

lock = threading.Lock()
server_id = -1


def handle_client(client_socket, address):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(f"Received from {address}: {message}")
        except ConnectionResetError:
            break
    print(f"Connection with {address} closed.")
    client_socket.close()


def server():
    lock.acquire()
    global server_id
    server_id = os.getpid()
    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)
    while True:
        port = int(input("Server port (10,000 - 20,000):"))
        if 10000 <= port <= 20000:
            break
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    lock.release()

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()


def client():
    lock.acquire()
    lock.release()
    while True:
        command = input("Enter command: ")
        split = command.split(' ')
        if split[0] == 'connect':
            host = split[1]
            port = int(split[2])
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
            while True:
                message = input("Enter command: ")
                message = message.split(' ', 1)
                if message[0].lower() == 'exit':
                    os.kill(server_id, signal.SIGINT)
                elif message[0].lower() == 'disconnect':
                    client_socket.close()
                    break
                elif message[0].lower() == 'send':
                    try:
                        client_socket.send(message[1].encode('utf-8'))
                    except IndexError:
                        print("Invalid message.")
                else:
                    print("Invalid command.")
            client_socket.close()
        elif split[0] == 'exit':
            os.kill(server_id, signal.SIGINT)
        elif split[0] == 'disconnect':
            print("Invalid. Haven't connected to a host yet.")
        elif split[0].lower() == "send":
            print("Invalid. Haven't connected to a host yet.")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    server_thread = threading.Thread(target=server)
    server_thread.start()

    client_thread = threading.Thread(target=client)
    clients = client_thread.start()

    server_thread.join()
    client_thread.join()
