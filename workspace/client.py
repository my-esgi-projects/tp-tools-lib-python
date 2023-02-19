#!/usr/bin/python
# coding: utf-8

import socket
from rich import print
from modules.client_utils import dict_menus,display_menu,display_submenu


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

def client_menu():
    # initialise server
    server = ("localhost", 8090)

    while True:
        choice = display_menu(dict_menus, color="green")

        if choice != "invalid":  
            while True:
                choices = display_submenu(dict_menus, main_menu_choice=choice)
                if choices[1] != "invalid":
                    if choices[1] == "0":
                        client_menu()
                    elif choices[1] == "yes":
                        quit()
                    elif choices[1] == "no":
                        client_menu()
                    else:
                        try:
                            client = Client(server)
                            request = '_'.join(choices)
                            response = client.send_message(request)
                            output = dict_menus[choices[0]]['submenu'][choices[1]]['final']
                            print(f"[bold blue] {output}{response}")
                        except Exception as exeption:
                            print(f"[bold red]{exeption}")
                            client_menu()
                else:
                    print("[bold magenta]Invalid choice.. Plz retry again")
        else:
            print("[bold magenta]Invalid choice.. Plz retry again")
            client_menu()

if __name__ == "__main__":
    
    client_menu()

    # response = client.send_message("Toto")
    # print(response)
