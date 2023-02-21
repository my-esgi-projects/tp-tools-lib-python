#!/usr/bin/python3

import os, subprocess
import argparse
from rich import print

"""
class user
"""


class User:
    def __init__(self, username, groupname) -> None:
        self.username = username
        self.groupname = groupname

    def is_user_exists_in_file(self) -> bool:
        try:
            with open("/etc/passwd", "r") as file:
                for line in file:
                    if self.username == line.split(":")[0]:
                        return True
                return False
        except Exception as exception:
            raise Exception(
                f"Something went wrong: failed to open file--->{str(exception)}"
            )

    def is_group_exists_in_file(self) -> bool:
        try:
            with open("/etc/group", "r") as file:
                for line in file:
                    if self.groupname == line.split(":")[0]:
                        return True
                return False
        except Exception as exception:
            raise Exception(
                f"Something went wrong: failed to open file--->{str(exception)}"
            )

    def is_user_exists(self) -> bool:
        command = ["getent", "passwd", self.username]
        user_check = subprocess.run(command, capture_output=True)

        if user_check.returncode == 0:
            return True
        else:
            return False

    def is_group_exists(self) -> bool:
        command = ["getent", "group", self.groupname]
        group_check = subprocess.run(command, capture_output=True)

        if group_check.returncode == 0:
            return True
        else:
            return False

    def create(self) -> str:
        try:
            if self.is_user_exists() and self.is_group_exists():
                return f"[bold blue]user {self.username} already exists"
            else:
                if not self.is_group_exists():
                    os.system(f"sudo groupadd {self.groupname}")

                if not self.is_user_exists():
                    os.system(f"sudo useradd {self.username}")

                os.system(f"sudo usermod -aG {self.groupname} {self.username}")
                return f"user {self.username} is create with success"

        except Exception as exception:
            raise Exception(f"Failed to create users and groups-->{str(exception)}")


"""
    functionnal code
"""


def create_from_file(file) -> None:
    try:
        with open(file, "r") as file:
            for line in file:
                username = str(line.split(":")[0]).strip()
                groupname = str(line.split(":")[1]).strip()
                user = User(username=username, groupname=groupname)
                msg = user.create()
                print(f"[bold green] {msg}")
    except Exception as exception:
        raise Exception(
            f"Failed to create users and groups from file-->{str(exception)}"
        )


def handle_args() -> tuple:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "-f", "--file", help="file which contains users and groups to create"
    )
    args = arg_parser.parse_args()
    return (args, arg_parser)


def main() -> None:
    try:
        args, arg_parser = handle_args()

        if args.file is None:
            arg_parser.print_help()
            quit()
        file = args.file
        create_from_file(file)
    except Exception as exception:
        print(f"[bold red] {exception}")


"""
run main method
"""
if __name__ == "__main__":
    main()
