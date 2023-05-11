#!/usr/bin/python
# coding: utf-8

import socket
import os
from threading import Thread
from lib.server_utils import function_output
from lib.client_utils import handle_args, default_port, default_host


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        Thread.__init__(self, group, target, name, args, kwargs, daemon=daemon)

        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        Thread.join(self)
        return self._return

class Server:
    def __init__(self, host=default_host, port=default_port) -> None:
        self.host = host
        self.port = port

    def create_server_socket(self) -> socket:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        return server_socket


def main(port=default_port, host=default_host) -> None:
    try:
        server = Server(host=host, port=port)
        server_socket = server.create_server_socket()

        while True:
            client_socket, client_address = server_socket.accept()
            client_response = client_socket.recv(1024)
            choice = str(client_response.decode())
        
            # create new thread
            thread = ThreadWithReturnValue(target=function_output, args=(choice,))
            thread.start()
            server_response = thread.join()
            
            # send response of server to client
            client_socket.send(b"" + server_response.encode())
    
            client_socket.close()

    except Exception as exception:
        raise Exception(f"Error with socket connexion-->{str(exception)}")


if __name__ == "__main__":
    try:
        args, arg_parser = handle_args()

        host = default_host if args.host is None else str(args.host)
        port = default_port if args.port is None else int(args.port)

        main(host=host, port=port)

    except Exception as exception:
        print(f"{str(exception)}")
