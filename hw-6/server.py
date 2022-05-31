"""server implementation"""

import socket
import threading
import json
import logging

from queue import Queue
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from collections import Counter

from html.parser import HTMLParser

from config import server_port

from utils import server_args_parser


class HTMLWordTop(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = ""

    def handle_data(self, data):
        self.data += f" {data}"

    def get_top(self):
        data = self.data
        self.data = ""
        return dict(Counter(data.split()).most_common(5))

    def error(self, message: str):
        pass


class Server:
    """sever implementation class"""
    def __init__(self, numb_of_workers, top_size):
        self.numb_of_workers = numb_of_workers
        self.top_size = top_size
        self.handled_urls = 0
        self.queue = Queue(10)

        self.workers = [
            threading.Thread(target=self.queue_worker, name=f"worker_{i}",
                             args=())
            for i in range(numb_of_workers)
        ]

    def info(self):
        """print information about handling"""
        self.handled_urls += 1
        print(f"Server has handled {self.handled_urls} urls")

    def start(self):
        """start server"""
        print("Server: server starts")

        for worker in self.workers:
            worker.start()

        sock = socket.socket()
        sock.bind(("", server_port))
        sock.listen(5)
        while True:
            client, _ = sock.accept()

            data = client.recv(4096)
            self.queue.put((data.decode("utf-8"), client))

    def queue_worker(self):
        """worker for Server class"""
        html_parser = HTMLWordTop()

        while True:
            url, client = self.queue.get()
            self.queue.task_done()

            try:
                resp = urlopen(url, timeout=2)
            except HTTPError:
                logging.error("Worker: connection error")
                client.send("connection error".encode())
            except URLError:
                logging.error("Worker: no address associated")
                client.send("Worker: no address associated with".encode())
            except socket.timeout:
                logging.error("Worker: the read operation timed out")
                client.send("The read operation timed out".encode())

            try:
                html_parser.feed(resp.read().decode())
                top = html_parser.get_top()
            except UnicodeDecodeError:
                logging.error("HTML parsing error")
                client.send("HTML parsing error".encode())
            except socket.timeout:
                logging.error("HTML parsing operation timed out")
                client.send("HTML parsing operation timed out".encode())

            most_common_json = json.dumps(top, indent=4, ensure_ascii=False)

            client.send(bytes(most_common_json, 'UTF-8'))

            self.info()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    args = server_args_parser()

    server = Server(args.w, args.k)
    server.start()
