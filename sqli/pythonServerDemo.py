#!/usr/bin/python3
import webbrowser
import argparse
import http.server
import socketserver
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="Port to run server on", type=int, default=9000, nargs='?')
    args = parser.parse_args()

    browse(str(args.port))

def server(port):
    handler = http.server.SimpleHTTPRequestHandler
    try:
        with socketserver.TCPServer(("", port,), handler) as httpd:
            print("serving at port {}".format(port))
            httpd.serve_forever()
    except OSError as error:
        print("Server could not bind, port still in use\n{}".format(error))

def browse(port):
    webbrowser.open_new('http://127.0.0.1:' + port + '/index.html')
    server(int(port))

if __name__ == "__main__":
    main()
