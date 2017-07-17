#!/usr/bin/env python3
import socket
import threading
import argparse

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
    run_server(bind_ip, args.port)


def run_server(bind_ip, bind_port):

    # Create server object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # Spin up server
        server.bind((bind_ip, bind_port))
        server.listen(1)
        print("[*] Listening on {}:{}".format(bind_ip, bind_port))
    
        # Set timeout
        server.settimeout(10)
    
        # Make connection with client
        client, address = server.accept()
        print("[*] Connection from {}:{}\n".format(address[0], address[1]))
    
        while True:
            request = client.recv(1024).decode('utf-8')
            if request in (".quit", ".exit"): break
            # Check for exit command
            print("[RECEIVED] {}".format(request))
    
        # Gracefully exit
        print("\nConnection terminated")

if __name__ == '__main__':
    main()
