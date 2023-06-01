#!/usr/bin/python
# coding: utf-8

from rich import print
from rich.prompt import Prompt
import argparse

default_host = ""
default_port = 8070


def display_menu(user_menu, color):
    for possibility in user_menu:
        print(f'[{color}]{user_menu[possibility]["label"]}')

    choice = str(Prompt.ask("[bold white]Enter your choice")).strip()
    if choice not in list(user_menu.keys()):
        return "invalid"
    else:
        return choice


def display_submenu(user_menu, main_menu_choice):
    if main_menu_choice in list(user_menu.keys()):
        dict_submenu = user_menu[main_menu_choice]["submenu"]

        return (main_menu_choice, display_menu(dict_submenu, "yellow"))
    else:
        return ("invalid", "invalid")


def handle_args() -> tuple:
    arg_parser = argparse.ArgumentParser(
        description="Launch without options will use localhost as default host and 8090 as defaut port"
    )
    arg_parser.add_argument("-H", "--host", help="server listen address")
    arg_parser.add_argument("-P", "--port", help="server listen port")
    args = arg_parser.parse_args()
    return (args, arg_parser)
