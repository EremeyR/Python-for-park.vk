"""client implementation"""

import socket
import threading

from config import server_port, urls_path

from utils import client_args_parser


def get_urls(path):
    """getting urls from file"""
    with open(path, 'r') as file:
        urls = file.read()
    return urls.split()


def client_thread():
    """thread for requests"""
    urls = get_urls(urls_path)
    for url in urls:
        sock = socket.socket()
        sock.connect(("", server_port))
        sock.sendall(url.encode())
        data = sock.recv(1024)
        print(f"{url}: {data.decode('utf8')}")


def client(numb_of_threads):
    """main thread"""
    threads = [
        threading.Thread(target=client_thread, name=f"clt_th_{i}", args=())
        for i in range(numb_of_threads)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    args = client_args_parser()

    urls_path = args.p
    client(args.m)
