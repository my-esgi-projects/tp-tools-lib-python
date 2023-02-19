#!/usr/bin/python
# coding: utf-8

import socket
import os
from modules.server_utils import function_output


class Server:
    def __init__(self, host="", port=8090) -> None:
        self.host = host
        self.port = port

    def create_server_socket(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        return server_socket


if __name__ == "__main__":
    server = Server(port=8090)
    server_socket = server.create_server_socket()

    while True:
        client_socket, client_address = server_socket.accept()
        pid = os.fork()
        if pid == 0:
            server_socket.close()
            client_response = client_socket.recv(1024)
            server_response = function_output(concat_choices=client_response.decode())
            # send response of server to client
            client_socket.send(b""+server_response.encode())
            client_socket.close()
            
            print(client_response.decode())
            os._exit(0)
        else:
            client_socket.close()
