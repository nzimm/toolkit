#!/usr/bin/env python3
import socket
import argparse
import time, random
from crypto import symmetric_encrypt
from primes import findPrimes


def main():
    # Local variables
    targetHost = "127.0.0.1"
    targetPort = 9999
    private_key = ''
    public_key = ''

    # Handle arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default=targetHost,
                        help="Target IPv4 host address (default {})".format(targetHost))
    parser.add_argument("--port", type=int, default=targetPort,
                        help="Port to connect to host on (default {})".format(targetPort))
    parser.add_argument("-e", "--encrypt", action='store_true', help="Encrypt connection to host")
    args = parser.parse_args()

    # Spin up client
    start_client(args.host, args.port, args.encrypt)


def encrypt_message(message, key):
    return symmetric_encrypt(message, key)


def start_client(targetHost, targetPort, encrypt):
    
    # Create socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    
        # Create connection
        client.connect((targetHost, targetPort))
        print("[*] Connection with {}:{}".format(targetHost, targetPort))
    
        # Set timeout
        client.settimeout(15)

        # Facilitate handshake
        if encrypt:
            client.send(bytes("CRYPT", 'utf-8'))
            if client.recv(4).decode('utf-8') == "ACK":
                encryption_key = "Test Key"
                print("[*] Handshake successful!\n[*] Transmition encrypted!")
            else:
                print("[*] Handshake failed!\nConnection terminated")
                client.send(bytes('.quit', 'utf-8'))
                client.close()
                exit(0)
        else:
            # Unencrypted handshake
            client.send(bytes("UCRYPT", 'utf-8'))
            if client.recv(4).decode('utf-8') == "ACK":
                print("[*] Handshake successful!\n[*] WARNING! Transmition unencrypted")
            else:
                print("[*] Handshake failed!\nConnection terminated")
                client.send(bytes('.quit', 'utf-8'))
                client.close()

    
        # On succsesful handshake successful
        print("[*] '.quit' to terminate connection\n")
        while True:
            # Prompt user for input
            message = input("[SEND] ")

            # Send encrypted message
            if encrypt:
                client.send(bytes(encrypt_message(message, encryption_key), 'utf-8'))
            
            # Send message
            else:
                client.send(bytes(message, 'utf-8'))
    
            # Check message against known commands
            if message in (".quit", ".q"): break
    
        # Gracefully exit 
        client.close()
        print("\nConnection with {} terminated".format(targetHost))


if __name__ == '__main__':
    main()
