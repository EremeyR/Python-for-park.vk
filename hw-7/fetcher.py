"""hw 7 - async fetcher"""
from collections import Counter
import asyncio
import argparse
from html.parser import HTMLParser

import aiohttp

QUEUE_SIZE = 10


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


def fetcher_args_parser():
    """args parser for server"""
    parser = argparse.ArgumentParser(description='fetcher_args')
    parser.add_argument('-c', type=int, default=10, help='number of workers')
    parser.add_argument("path_to_urls", type=str, default="urls.txt.txt",
                        help='file with urls.txt')
    return parser.parse_args()


async def load_urls(urls_queue, path_to_urls):
    """async urls.txt loading from file"""
    with open(path_to_urls, "r", encoding="utf-8") as file:
        for url in file:
            await urls_queue.put(url.rstrip())


async def fetch(client, urls_queue):
    """infinite event loop with urls.txt fetching"""

    parser = HTMLWordTop()

    try:
        while True:
            url = await urls_queue.get()
            try:
                async with client.get(url) as resp:
                    data = await resp.text()
                    parser.feed(data)
                    top = parser.get_top()
                    print(f"{url}:\n {top}")
            finally:
                urls_queue.task_done()
    except StopIteration:
        #  try is needed to exit the loop during testing
        pass


async def fetch_urls(requests_count, path_to_urls):
    """start function"""
    urls_queue = asyncio.Queue(maxsize=QUEUE_SIZE)
    load_urls_task = asyncio.create_task(load_urls(urls_queue, path_to_urls))

    async with aiohttp.ClientSession() as client:
        tasks = [
            asyncio.create_task(fetch(client, urls_queue))
            for _ in range(requests_count)
        ]

        await load_urls_task
        await urls_queue.join()

    for task in tasks:
        task.cancel()
    load_urls_task.cancel()


if __name__ == "__main__":
    args = fetcher_args_parser()
    asyncio.run(fetch_urls(args.c, args.path_to_urls))
