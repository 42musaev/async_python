import socket
from select import select

to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('0.0.0.0', 5000))
server_socket.listen()


def accept_connection(host_socket: socket.socket) -> None:
    client_socket, address = host_socket.accept()
    to_monitor.append(client_socket)


def send_message(client_socket: socket.socket) -> None:
    request = client_socket.recv(4096)
    if request:
        message = b'I got the message\n'
        client_socket.send(message)
    else:
        client_socket.close()


def event_loop() -> None:
    while True:
        ready_to_read, _, _ = select(to_monitor, [], [])
        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == '__main__':
    to_monitor.append(server_socket)
    event_loop()
