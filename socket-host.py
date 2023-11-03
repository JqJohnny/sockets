import socket
import threading
import time

def handle_client(client_socket, address):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received from {address}: {data.decode('utf-8')}")
        except ConnectionResetError:
            break
    print(f"Connection with {address} closed.")
    client_socket.close()


def server():
    hostname = socket.gethostname()
    host = socket.gethostbyname(hostname)
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()


def client():
    host = input("Enter IP: ")
    port = int(input("Enter port: "))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        time.sleep(0.5)
        message = input("Enter message: ")
        if message.lower() == 'exit':
            break
        elif message.lower() == 'disconnect':
            client_socket.close()
            break
        else:
            client_socket.send(message.encode('utf-8'))


if __name__ == "__main__":
    server_thread = threading.Thread(target=server)
    server_thread.start()

    time.sleep(0.5)

    client_thread = threading.Thread(target=client)
    client_thread.start()

    server_thread.join()
    client_thread.join()

