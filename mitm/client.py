#!/usr/bin/env python3
import socket
import argparse

# Default values
targetHost = "127.0.0.1"
targetPort = 9999

# Parse inputs
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--server", type=str, default=targetHost,
                    help="Target IPv4 host address (default {})".format(targetHost))
parser.add_argument("-p", "--port", type=int, default=targetPort,
                    help="Port to connect to host on (default {})".format(targetPort))
args = parser.parse_args()


# Create socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

    # Set timeout
    client.settimeout(10)

    # Create connection
    client.connect((args.server, args.port))

    # Initiate handshake
    client.send(bytes('SYN', 'utf-8'))
    responce = client.recv(3).decode('utf-8')

    # Check for correct responce
    if responce != 'ACK':
        print("Server did not acknowledge, shutting down connection")
        exit(1)
    
