import socket
import selectors

selector = selectors.DefaultSelector()


def server() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 5000))
    server_socket.listen()
    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(server_socket: socket.socket) -> None:
    client_socket, address = server_socket.accept()
    print(f'connection from: {address}')
    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)


def send_message(client_socket: socket.socket) -> None:
    request = client_socket.recv(4096)
    if request:
        client_socket.send(b'I got the message')
    else:
        selector.unregister(fileobj=client_socket)
        client_socket.close()


def event_loop() -> None:
    while True:
        events = selector.select()
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    server()
    event_loop()
