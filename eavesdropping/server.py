#!/usr/bin/env python3
import socket
import threading
import argparse
from crypto import symmetric_decrypt

def main():
    # Default values
    bind_ip = "0.0.0.0"
    bind_port = 9999

    # Parse inputs
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=bind_port,
                        help="Port to connect to host on (default{})".format(bind_port))
    args = parser.parse_args()

    # Spin up server
    start_server(bind_ip, args.port)


def decrypt_message(message, key):
    return symmetric_decrypt(message, key)

def start_server(bind_ip, bind_port):

    # Create server object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # Spin up server
        server.bind((bind_ip, bind_port))
        server.listen(1)
        print("[*] Listening on {}:{}".format(bind_ip, bind_port))
    
        # Set timeout
        server.settimeout(10)
    
        # Make connection with client
        connection, address = server.accept()
        print("[*] Connection from {}:{}".format(address[0], address[1]))

        # Facilitate handshake
        handshake = connection.recv(8).decode('utf-8')
        encrypted = False
        if handshake == "UCRYPT":
            connection.send(bytes("UACC", 'utf-8'))
            print("[*] Handshake succsesful!\n")
        elif handshake == "CRYPT":
            #TODO write encryption handshake
            connection.send(bytes("ACC", 'utf-8'))
            encrypted = True
            decryption_key = "Test Key"
        else:
            print("Handshake failed. Connection terminated")
            exit(0)
    
        while True:
            # Receive message
            message = connection.recv(1024).decode('utf-8')

            # Decrypt message
            if encrypted:
                message = decrypt_message(message, decryption_key)

            # Check for exit command
            if message in (".quit", ".q"): break

            print("[RECEIVED] {}".format(message))
    
        # Gracefully exit
        print("\nConnection terminated")

if __name__ == '__main__':
    main()
