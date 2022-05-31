"""tests for LRUCache"""
import unittest

import implementation as implt


def check_condition(cache, condition):
    """
    :param cache: LRUCache instance
    :param condition: list with nods values e.g. [["k1", "v1"], ["k2", "v2"]]
    :return: True if cache nods == condition list
    """
    i = 0
    cur_node = cache.head
    while cur_node:
        if cur_node.key != condition[i][0] or \
                cur_node.value != condition[i][1]:
            return False
        i += 1
        cur_node = cur_node.next
    return True


class TestStringMethods(unittest.TestCase):
    """unit tests for LRUCache"""
    def test_1(self):
        """simple test"""
        cache = implt.LRUCache()
        cache.set(1, 111)
        cache.set(2, 222)

        self.assertTrue(check_condition(cache, [[2, 222], [1, 111]]))

    def test_2(self):
        """test with displacement"""
        cache = implt.LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertEqual(cache.get("k3"), None)
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k3", "val3")

        self.assertEqual(cache.get("k3"), "val3")
        self.assertEqual(cache.get("k2"), None)
        self.assertEqual(cache.get("k1"), "val1")

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

    def test_7(self):
        """test with complete displacement"""
        cache = implt.LRUCache(3)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")

        cache.set("k1_new", "val1_new")
        cache.set("k2_new", "val2_new")
        cache.set("k3_new", "val3_new")

        self.assertTrue(check_condition(cache, [["k3_new", "val3_new"],
                                                ["k2_new", "val2_new"],
                                                ["k1_new", "val1_new"]]))

    def test_8(self):
        """test with complete displacement"""
        cache = implt.LRUCache(3)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")

        cache.set("k1_new", "val1_new")
        cache.set("k2_new", "val2_new")
        cache.set("k3_new", "val3_new")

        self.assertTrue(check_condition(cache, [["k3_new", "val3_new"],
                                                ["k2_new", "val2_new"],
                                                ["k1_new", "val1_new"]]))

    def test_9(self):
        """test with complete displacement after one rewriting"""
        cache = implt.LRUCache(3)

        cache.set("k1", "val1")
        cache.set("k2", "val2")
        cache.set("k3", "val3")

        cache.set("k2", "val2_new")

        self.assertTrue(check_condition(cache, [["k2", "val2_new"],
                                                ["k3", "val3"],
                                                ["k1", "val1"]]))

        cache.set("k4", "val4")
        cache.set("k5", "val5")

        self.assertTrue(check_condition(cache, [["k5", "val5"],
                                                ["k4", "val4"],
                                                ["k2", "val2_new"]]))

        cache.set("k6", "val6")

        self.assertTrue(check_condition(cache, [["k6", "val6"],
                                                ["k5", "val5"],
                                                ["k4", "val4"]]))


if __name__ == '__main__':
    unittest.main()
