"""client implementation"""

import socket
import threading

from config import server_port

from utils import client_args_parser


def get_urls(path):
    """getting urls from file"""
    with open(path, 'r') as file:
        urls = file.read()
    return urls.split()


class Client:
    """client implementation class"""
    def __init__(self, numb_of_threads, urls_path):
        self.numb_of_threads = numb_of_threads
        self.urls_path = urls_path

    def start(self):
        """main thread"""
        threads = [
            threading.Thread(target=self.client_thread,
                             name=f"clt_th_{i}", args=())
            for i in range(self.numb_of_threads)
        ]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    def client_thread(self):
        """thread for requests"""
        urls = get_urls(self.urls_path)
        for url in urls:
            sock = socket.socket()
            sock.connect(("", server_port))
            sock.sendall(url.encode())
            data = sock.recv(1024)
            print(f"{url}: {data.decode('utf8')}")


if __name__ == "__main__":
    args = client_args_parser()

    client = Client(args.m, args.p)
    client.start()
