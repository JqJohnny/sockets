import socket
import threading

lock = threading.Lock()


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
    host = input("Enter IP: ")
    port = int(input("Enter port: "))
    lock.release()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Enter message: ")
        if message.lower() == 'exit':
            client_socket.send(message.encode('utf-8'))
            break
        elif message.lower() == 'disconnect':
            client_socket.close()
            break
        else:
            client_socket.send(message.encode('utf-8'))
    client_socket.close()


if __name__ == "__main__":
    server_thread = threading.Thread(target=server)
    server_thread.start()

    client_thread = threading.Thread(target=client)
    client_thread.start()

    server_thread.join()
    client_thread.join()

