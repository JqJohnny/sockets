# Python Socket Programming Project

## Overview

This project demonstrates basic TCP socket communication in Python using client-server architecture and multithreading.

The programs allow clients and servers to communicate over a network using TCP sockets. The project was used to grasp concepts such as concurrent connections, message transmission, and thread-based connection handling.

---

## Files

### `socket-client.py`
A TCP client application that:
- connects to a server using an IP address and port
- sends messages to the server
- supports a quit command for closing the connection

---

### `socket-server.py`
A basic TCP server that:
- listens for incoming client connections
- receives messages from connected clients
- logs messages received from the client
- returns stored messages when the client disconnects

---

### `socket-host.py`
A multithreaded socket application that:
- handles multiple client connections using threads
- supports commands such as:
  - `connect`
  - `send`
  - `disconnect`
  - `exit`
- manages concurrent communication between clients and the server

---

## Technologies Used

- Python
- TCP sockets
- Multithreading

---

## Concepts Demonstrated

- TCP/IP communication
- Client-server architecture
- Socket programming
- Multithreading
- Concurrent connection handling
- Network communication fundamentals

---

## Running the Programs

### Run the Server

```bash
python socket-server.py
