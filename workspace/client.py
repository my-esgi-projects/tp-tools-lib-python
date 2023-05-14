#!/usr/bin/python
# coding: utf-8

import socket
from rich import print
from lib.client_utils import (
    display_menu,
    display_submenu,
    handle_args,
    default_host,
    default_port,
)
from lib.menu import dict_menus


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


def client_menu(host=default_host, port=default_port):

    # initialise server
    server = (host, port)

    while True:
        choice = display_menu(dict_menus, color="green")

        if choice != "invalid":
            while True:
                choices = display_submenu(dict_menus, main_menu_choice=choice)

                if choices[1] != "invalid":
                    if choices[1] == "0":
                        client_menu(host=host, port=port)

                    elif choices[1] == "yes":
                        quit()

                    elif choices[1] == "no":
                        client_menu(host=host, port=port)

                    else:
                        try:
                            client = Client(server)
                            request = "_".join(choices)
                            response = client.send_message(request)
                            output = dict_menus[choices[0]]["submenu"][choices[1]][
                                "final"
                            ]
                            print(f"[bold blue] {output}{response}")
                        except Exception as exeption:
                            print(f"[bold red]{exeption}")
                            client_menu(host=host, port=port)

                else:
                    print("[bold magenta]Invalid choice.. Plz retry again")

        else:
            print("[bold magenta]Invalid choice.. Plz retry again")
            client_menu(host=host, port=port)


if __name__ == "__main__":

    try:
        args, arg_parser = handle_args()

        host = default_host if args.host is None else str(args.host)
        port = default_port if args.port is None else int(args.port)

        client_menu(host=host, port=port)

    except Exception as exception:
        print(f"{str(exception)}")
