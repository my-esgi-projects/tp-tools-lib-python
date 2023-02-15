# coding: utf-8

import socket


class Client:
    def __init__(self, server) -> None:
        self.server = server

    def send_message(self, message):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((self.server))
        client_socket.sendall(message.encode())
        response = client_socket.recv(1024)
        client_socket.close()
        return response.decode()


if __name__ == "__main__":
    server = ("localhost", 8090)
    client = Client(server)

    response = client.send_message("Toto")
    print(response)
