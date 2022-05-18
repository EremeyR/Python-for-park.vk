"""hw 7 - async fetcher"""
from collections import Counter
import re
import asyncio
import argparse
import logging
import json

import html2text
import aiohttp


def server_args_parser():
    """args parser for server"""
    parser = argparse.ArgumentParser(description='fetcher_args')
    parser.add_argument('-c', type=int, default=10, help='number of workers')
    parser.add_argument("path_to_urls", type=str, default="urls.txt",
                        help='file with urls')
    return parser.parse_args()


def html_to_text(html):
    """convert html to text"""
    html_parser = html2text.HTML2Text()
    html_parser.ignore_links = True
    html_parser.ignore_images = True
    html_parser.ignore_tables = True
    html_parser.ignore_emphasis = True

    text = html_parser.handle(html)
    text = re.sub(r'[^\w\s]', '', text)

    return text


def get_top5(text):
    """find the top 5 most common words"""
    _dict = dict(Counter(text.split()).most_common(5))

    return json.dumps(_dict, indent=4, ensure_ascii=False)


async def load_urls(urls_queue, path_to_urls):
    """async urls loading from file"""
    with open(path_to_urls, "r", encoding="utf-8") as file:
        for url in file:
            await urls_queue.put(url.rstrip())


async def fetch(client, urls_queue):
    """infinite event loop with urls fetching"""
    while True:
        url = await urls_queue.get()
        try:
            async with client.get(url) as resp:
                data = await resp.text()
                words = html_to_text(data)
                top = get_top5(words)
                print(f"{url}: {top}")
        except aiohttp.web.HTTPException as error:
            logging.error("Url getting error: %s", error)
        finally:
            urls_queue.task_done()


async def fetch_urls(requests_count, path_to_urls):
    """start function"""
    urls_queue = asyncio.Queue()
    await load_urls(urls_queue, path_to_urls)

    async with aiohttp.ClientSession() as client:
        tasks = [
            asyncio.create_task(fetch(client, urls_queue))
            for _ in range(requests_count)
        ]
        await urls_queue.join()

    for task in tasks:
        task.cancel()


if __name__ == "__main__":
    args = server_args_parser()
    asyncio.run(fetch_urls(args.c, args.path_to_urls))
