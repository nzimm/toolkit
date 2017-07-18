#!/usr/bin/env python3
import subprocess
import threading
from binascii import unhexlify
    
def sniff(time):
    """ Call tshark (CLI for Wireshark) to sniff packets on loopback """

    result = subprocess.run(['tshark', '-i', 'lo', '-T', 'fields', '-e', 'data',
                             '-q', '-a', 'duration:'+time], stdout=subprocess.PIPE)
    for data in result.stdout.decode().split('\n'):
        clean_data = unhexlify(data).decode()
        if clean_data != '':
            print("[SNIFFED DATA] {}".format(clean_data))

def main():
    while True:
        user_input = input("\nSniff packets? (help for options) ").lower()

        # Print help message
        if user_input in ('h', 'help'):
            print('\nSniffer demonstration application. Using wireshark, message data is')
            print('passively picked up and displayed.\n')
            print('yes:   sniff packets from loopback (localhost)')
            print('no:    quit program')
            print('help:  display this help message\n')
        
        # Ask user for length of time to sniff packets
        elif user_input in ('y', 'yes'):
            while True:
                time = input("Sniff packets for how many seconds? ")
                try:
                    if int(time) > 0:
                        pass
                except ValueError as err:
                    print("{}: Please enter a valid number".format(err))
                sniff(time)
                break

        # Gracefully exit
        elif user_input in ('no', 'n', 'exit', 'quit'):
            exit(0)

        # Handle non-standard input
        else:
            print("{} is not a valid input. Enter 'help' for options".format(user_input))
            
if __name__ == '__main__':
    main()
