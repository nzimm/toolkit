#!/usr/bin/env python3
import socket
import argparse

def main():
    # Variables
    targetHost = "127.0.0.1"
    targetPort = 9999

    # Handle arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default=targetHost,
                        help="Target IPv4 host address (default {})".format(targetHost))
    parser.add_argument("--port", type=int, default=targetPort,
                        help="Port to connect to host on (default {})".format(targetPort))
    parser.add_argument("-e", "--encrypt", action='store_true')
    args = parser.parse_args()

    # Spin up client
    start_client(args.host, args.port, args.encrypt)


def encrypt_message(message, encryption_key):
    #TODO write encryption message
    return message


def start_client(targetHost, targetPort, encrypt):
    
    # Create socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    
        # Create connection
        client.connect((targetHost, targetPort))
        print("[*] Connection with {}:{}".format(targetHost, targetPort))
    
        # Set timeout
        # NOTE: Figure out why client doesn't timeout - while loop resets counter?
        client.settimeout(3)

        # Facilitate handshake
        if encrypt:
            #TODO write encryption handshake
            encryption_key = ""
        else:
            # Unencrypted handshake
            client.send(bytes("UCRYPT", 'utf-8'))
            if client.recv(3).decode('utf-8') == "ACC":
                print("[*] Handshake successful!")

    
        # On succsesful handshake successful
        print("[*] '.quit' to terminate connection\n")
        while True:
            # Prompt user for input
            message = input("[SEND] ")

            # Encrypt message
            if encrypt:
                message = encrypt_message(message, encryption_key)

            # Send message
            client.send(bytes(message, 'utf-8'))
    
            # Check message against known commands
            if message in (".quit", ".q"): break
    
        # Gracefully exit 
        client.close()
        print("\nConnection with {} terminated".format(targetHost))


if __name__ == '__main__':
    main()
