import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('0.0.0.0', 5000))
server_socket.listen()

while True:
    client_socket, address = server_socket.accept()
    while True:
        request = client_socket.recv(4096)
        if request:
            message = b'I got the message\n'
            client_socket.send(message)
        else:
            break
    client_socket.close()
