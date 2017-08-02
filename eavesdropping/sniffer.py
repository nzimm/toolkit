#!/usr/bin/env python3
import subprocess
import threading
from binascii import unhexlify
    
def sniff(time):
    """ Call tshark (CLI for Wireshark) to sniff packets on loopback """
    #TODO replase [SNIFFED DATA] with [CLIENT->SERVER] or visa versa (handshake)

    print("\nInitiating Wireshark")
    result = subprocess.run(['tshark', '-i', 'lo', '-T', 'fields', '-e', 'data',
                             '-q', '-a', 'duration:'+time], stdout=subprocess.PIPE)
    for data in result.stdout.decode().split('\n'):
        clean_data = unhexlify(data).decode()
        if clean_data != '':
            print("[SNIFFED DATA] {}".format(clean_data))
#    result = subprocess.run(['tshark', '-i', 'lo', '-T', 'fields', '-e', 'data',
#                             '-e', 'tcp.port', '-e', 'ip.src_addr', '-q', '-a',
#                             'duration:'+time], stdout=subprocess.PIPE)
#    for line in result.stdout.decode().split('\n'):
#        for data in line.split('\t'):
#            clean_data = unhexlify(data).decode()
#            if clean_data != '':
#                print("[SNIFFED DATA] {}".format(clean_data))

def menu(time):
    """ Print menu option """
    print("\n===== Packet Sniffer =====")
    print("[1] Begin capturing packet data ({} seconds)".format(time))
    print("[2] Specify capture length")
    print("[3] Display sniffer information")
    print("[4] Quit")


def main():
    # Main menue loop
    sniffTime = '15'
    while True:
        menu(sniffTime)
        user_input = input("\n\nPlease input choice (1-4): ").lower()

        # Sniff for 15 seconds
        if user_input == "1":
            sniff(sniffTime)

        # Poll user for time
        elif user_input == "2":
            while True:
                time = input("\nHow many seconds would you like to sniff for? ")
                try:
                    if int(time) >= 0:
                        pass
                except ValueError as err:
                    print("{}: Please enter a valid number".format(err))
                sniffTime = time
                break
             
        # Print help message
        elif user_input == "3":
            print('\nPasive eavsdroping demo. Using the Wireshark command line interface,')
            print('message data is captured, decoded and displayed. Packets contain')
            print('control information which is not displayed for simplicity.\n')
            print('This application serves to demonstrate the feasibility of passive')
            print('eavsdropping, and the importance of encryption. The defualt interface')
            print('being tapped is the loopback, as the defualt client/server connection')
            print('is over 127.0.0.1')
        
        # Gracefully exit
        elif user_input in ("4", "exit", "quit"):
            print("Terminating...")
            exit(0)

        # Handle non-standard input
        else:
            print("{} is not a valid input. Please consult menu for options".format(user_input))
            
if __name__ == '__main__':
    main()
