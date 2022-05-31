import unittest
import asyncio

import fetcher


async def prt():
    print(1)


class MockClient:
    class Resp:
        def __enter__(self):
            return self

        async def __aenter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            pass

        def __init__(self, url):
            self.html = f"<{url}>" \
                        f"one two three four two three four three four four _" \
                        f"</{url}>"

        async def text(self):
            return self.html

    def get(self, url):
        resp = self.Resp(url)
        return resp

    def set(self):
        pass


class MockQueue:
    def __init__(self, mock_url, count):
        self.count = count
        self.mock_url = mock_url

    def __len__(self):
        return self.count

    async def get(self):
        return f"{self.mock_url} {self.count}"

    async def put(self):
        self.count += 1

    def task_done(self):
        self.count -= 1
        if self.count == 0:
            raise StopIteration


async def test_fetch(unit_test, queue_size):
    client = MockClient()
    queue = MockQueue("mock_url.com", queue_size)

    await fetcher.fetch(client, queue)

    unit_test.assertEqual(len(queue), 0)


async def test_load_urls(unit_test):
    queue = MockQueue("mock_url.com", 0)
    await fetcher.load_urls(queue, "test_urls.txt")

    unit_test.assertEqual(len(queue), 10)


async def test_general(unit_test):
    queue = MockQueue("mock_url.com", 0)
    client = MockClient()

    await fetcher.load_urls(queue, "test_urls.txt")

    unit_test.assertEqual(len(queue), 10)

    await fetcher.fetch(client, queue)

    unit_test.assertEqual(len(queue), 0)


class TestStringMethods(unittest.TestCase):
    def test_fetch_queue(self):
        asyncio.run(test_fetch(self, 100))

    def test_load_urls(self):
        asyncio.run(test_load_urls(self))

    def test_general(self):
        asyncio.run(test_general(self))


if __name__ == '__main__':
    unittest.main()
