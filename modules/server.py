# coding: utf-8
import socket
import os


class Server:
    def __init__(self, host="", port=8090) -> None:
        self.host = host
        self.port = port

    def _construct_client_response(self, choice):
        pass

    def _handle_client_request(self, client_socket):
        response = client_socket.recv(1024)
        # send client response
        client_socket.send(b"ACK")
        client_socket.close()
        return response

    def _create_server_socket(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        return server_socket

    def handle_and_accept_connexion(self):
        # Accept and handle client requests
        server_socket = self._create_server_socket()

        while True:
            client_socket, client_address = server_socket.accept()
            pid = os.fork()
            if pid == 0:
                server_socket.close()
                response = self._handle_client_request(client_socket)

                if response != "":
                    print(response.decode())
                os._exit(0)
            else:
                client_socket.close()


if __name__ == "__main__":
    server = Server(port=8090)
    server.handle_and_accept_connexion()
