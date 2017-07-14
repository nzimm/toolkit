#!/usr/bin/env python3
import socket
import threading
import argparse

# Default values
bind_ip = "0.0.0.0"
bind_port = 9999

# Parse inputs
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", type=int, default=bind_port, help="Port to connect to host on (default{})".format(bind_port))
args = parser.parse_args()


# Client-handling thread
def handle_client(client_socket):
    
    # Print data from client
    request = client_socket.recv(1024).decode('utf-8')
    print("Received: {}".format(request))

    # Return responce to client
    client_socket.send(bytes('ACK', 'utf-8'))
    client_socket.close()


# Create server object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    # Spin up server
    server.bind((bind_ip, bind_port))
    server.listen(1)
    print("Listening on {}:{}".format(bind_ip, bind_port))

    # Set timeout
    server.settimeout(10)

    while True:

        # Make connection with client
        client, address = server.accept()
        print("Connection from {}:{}".format(address[0], address[1]))
    
        # Spin up client thread
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
