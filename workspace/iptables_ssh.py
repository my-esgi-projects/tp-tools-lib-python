#!/usr/bin/python
from paramiko import SSHClient, AutoAddPolicy
from rich import print
from argparse import ArgumentParser
import logging, time


class ParmikoSsh:
    def __init__(self, hostname: str, username: str, port=22, password=None) -> None:
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    def run(self, file: str, log_file="./ssh_log.txt") -> None:

        try:
            logging.basicConfig(
                filename=log_file,
                format="%(levelname)s %(asctime)s %(message)s",
                level=logging.DEBUG,
            )

            rules = Rules(file=file)
            logging.info(rules.load_rules())

            for command in rules.load_rules():
                ssh_client = SSHClient()
                ssh_client.set_missing_host_key_policy(AutoAddPolicy())
                ssh_client.connect(
                    hostname=self.hostname,
                    port=self.port,
                    username=self.username,
                    password=self.password,
                )

                stdin, stdout, stderr = ssh_client.exec_command(f"sudo {command}")

                print(f"Sending command: [green]{command}")
                time.sleep(1)
                print(f"Output: [yellow]{stdout.readlines()}")

                if stderr.readlines():
                    print(f"Error: [red]{stderr.readlines()}")
                    logging.error(f"command: {command} -> stderr: {stderr.readlines()}")

                logging.info(f"command: {command} -> stdout: {stdout.readlines()}")

        except Exception as exception:
            raise Exception(f"Something went wrong with ssh connexion:-> {exception}")


class Rules:
    def __init__(self, file: str) -> None:
        self.file = file

    def load_rules(self) -> list:
        rules = list()
        try:
            with open(f"{self.file}", "r") as file:
                for line in file:
                    if not line.startswith("#") and line != "":
                        rules.append(line.rstrip())

            return rules

        except Exception as exception:
            raise Exception(f"Unable to read rules from file used.. -> {exception}")


def handle_args():
    try:
        arg_parser = ArgumentParser(
            description="Execute commands througth ssh",
            prog="iptables_ssh",
            usage="%(prog)s [options]",
        )
        arg_parser.add_argument(
            "-H", "--host", help="Server for ssh connexion", required=True, type=str
        )
        arg_parser.add_argument(
            "-U",
            "--username",
            help="Username for login to the server",
            required=True,
            type=str,
        )
        arg_parser.add_argument(
            "-P",
            "--password",
            help="Password for login to the server",
            required=True,
            type=str,
        )
        arg_parser.add_argument(
            "-F",
            "--file",
            help="Path to file which contains commands",
            required=True,
            type=str,
        )
        arg_parser.add_argument(
            "-L", "--log", help="Path to file for logging all informations", type=str
        )

        args = arg_parser.parse_args()

        return args

    except Exception as exception:
        logging.error(f"{exception}")
        raise Exception(f"Something went wrong during argument parsing {exception}")


if __name__ == "__main__":

    try:
        args = handle_args()
        file = "files/rules.txt"
        para = ParmikoSsh(
            hostname=args.host, username=args.username, password=args.password
        )

        para.run(
            file=args.file,
            log_file=args.log if args.log is not None else "./ssh_log.txt",
        )

    except Exception as exception:
        logging.error(f"{exception}")
        print(f"[bold red] {exception}")
