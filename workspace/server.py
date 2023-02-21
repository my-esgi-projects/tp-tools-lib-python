#!/usr/bin/python
# coding: utf-8

import socket
import os
import argparse
from modules.server_utils import function_output
from modules.client_utils import handle_args


class Server:
    def __init__(self, host="", port=8090) -> None:
        self.host = host
        self.port = port

    def create_server_socket(self) -> socket:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        return server_socket


def main(port=8090, host="") -> None:
    try:
        server = Server(host=host, port=port)
        server_socket = server.create_server_socket()

        while True:
            client_socket, client_address = server_socket.accept()
            pid = os.fork()
            if pid == 0:
                server_socket.close()
                client_response = client_socket.recv(1024)
                server_response = function_output(
                    concat_choices=client_response.decode()
                )
                # send response of server to client
                client_socket.send(b"" + server_response.encode())
                client_socket.close()

                # print(client_response.decode())
                os._exit(0)
            else:
                client_socket.close()

    except Exception as exception:
        raise Exception(f"Error with socket connexion-->{str(exception)}")


if __name__ == "__main__":
    try:
        args, arg_parser = handle_args()

        if args.host is None and args.port is None:
            main()
        else:
            host = ""
            port = 8090
            if args.host is not None:
                host = str(args.host)

            if args.port is not None:
                port = int(args.port)

            main(host=host, port=port)

    except Exception as exception:
        print(f"{str(exception)}")
