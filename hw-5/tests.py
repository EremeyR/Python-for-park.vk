"""tests for LRUCache"""
import unittest

import implementation as implt


class TestStringMethods(unittest.TestCase):
    """unit tests for LRUCache"""
    def test_1(self):
        """simple test"""
        cache = implt.LRUCache()
        cache.set(1, 111)
        cache.set(2, 222)

        self.assertEqual(cache.get(1), 111)
        self.assertEqual(cache.get(2), 222)
        self.assertEqual(cache.get(3), None)

    def test_2(self):
        """test with displacement"""
        cache = implt.LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k3"), None)

        cache.set("k3", "val3")

        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k3"), "val3")

    def test_3(self):
        """test with had and tail rewriting"""
        cache = implt.LRUCache(2)

        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.get("k2"), "val2")

        cache.set("k2", "val2_new")

        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.get("k2"), "val2_new")

        cache.set("k1", "val1_new")

        self.assertEqual(cache.get("k1"), "val1_new")

    def test_4(self):
        """test with middle node rewriting"""
        cache = implt.LRUCache(3)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")

        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k3"), "val3")

        cache.set("k2", "val2_new")

        self.assertEqual(cache.get("k1"), "val1")
        self.assertEqual(cache.get("k2"), "val2_new")
        self.assertEqual(cache.get("k3"), "val3")

    def test_5(self):
        """test with one node displacement"""
        cache = implt.LRUCache(1)

        cache.set("k1", "val1")

        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k2", "val2")

        self.assertEqual(cache.get("k1"), None)
        self.assertEqual(cache.get("k2"), "val2")

    def test_6(self):
        """test with one node rewriting"""
        cache = implt.LRUCache()

        cache.set("k1", "val1")

        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k1", "val1_new")

        self.assertEqual(cache.get("k1"), "val1_new")


if __name__ == '__main__':
    unittest.main()
