#!/usr/bin/python

from pyshark import LiveCapture
from scapy.all import sniff
from argparse import ArgumentParser

protocols = ['http', 'dns', 'tcp', 'udp', 'icmp']

def pyshark_capture(interface, display_filter):
    capture = LiveCapture(interface=interface, display_filter=display_filter)

    for packet in capture.sniff_continuously():
        print(packet)

def scapy_capture(protocol):
    sniff(filter=protocol, prn=lambda x:x.summary(), count=5)


def main():
    print("Mini WireShark - Select protocol to filter:")
    for i, protocol in enumerate(protocols, start=1):
        print(f"{i}. {protocol} filtering")
    print("0. Quit")

    choice = int(input("Entrez le numéro du protocole : "))

    if choice == 0:
        quit()

    if choice < 1 or choice > len(protocols):
        print("Choix invalide. Veuillez réessayer.")
        main()
    
    print("1. Scan avec scappy")
    print("2. Scan with pyshark")

    subchoice = int(input("Entrez l'outils de filtrage: "))
    
    if subchoice not in [1,2]:
        print("Choix invalide. Retour au menu principal")
        main()
    
    display_filter = protocols[choice - 1]
    
    if subchoice == 1:
        scapy_capture(display_filter)
    else:
        pyshark_capture('any', display_filter)


if __name__ == '__main__':
    try:
        main()
    except Exception as exception:
        print(f"Something went wrong: {exception}")
        main()
