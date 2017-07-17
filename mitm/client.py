#!/usr/bin/env python3
import socket
import argparse

def main():
    # Variables
    targetHost = "127.0.0.1"
    targetPort = 9999

    # Handle arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--server", type=str, default=targetHost,
                        help="Target IPv4 host address (default {})".format(targetHost))
    parser.add_argument("-p", "--port", type=int, default=targetPort,
                        help="Port to connect to host on (default {})".format(targetPort))
    args = parser.parse_args()

    # Spin up client
    run_client(args.server, args.port)


def run_client(targetHost, targetPort):
    
    # Create socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    
        # Set timeout
        client.settimeout(10)
    
        # Create connection
        client.connect((targetHost, targetPort))
        print("[*] Connection with {}:{}\n".format(targetHost, targetPort))

    
        # Handshake successful
        print("Send .quit or .exit to quit")
        while True:
            message = input("[SEND] ")
            client.send(bytes(message, 'utf-8'))
    
            # Check message against known commands
            if message in (".quit", ".exit"): break
    
        # Gracefully exit 
        client.close()
        print("\nConnection with {} terminated".format(targetHost))


if __name__ == '__main__':
    main()
