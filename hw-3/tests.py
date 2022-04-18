import unittest
from custom_list import CustomList

class TestStringMethods(unittest.TestCase):
    def test_sum_func(self):
        cust_lst = CustomList([1])
        self.assertEqual(cust_lst.sum(), 1)

        cust_lst = CustomList([1, 2, 3])
        self.assertEqual(cust_lst.sum(), 6)

        cust_lst = CustomList([-1])
        self.assertEqual(cust_lst.sum(), -1)

        cust_lst = CustomList([-40, -2])
        self.assertEqual(cust_lst.sum(), -42)

        cust_lst = CustomList([-50, 8])
        self.assertEqual(cust_lst.sum(), -42)

        cust_lst = CustomList([])
        self.assertEqual(cust_lst.sum(), 0)

        cust_lst = CustomList([0])
        self.assertEqual(cust_lst.sum(), 0)

        cust_lst = CustomList([0, 0, 0, 0])
        self.assertEqual(cust_lst.sum(), 0)

        cust_lst = CustomList([-42, 42])
        self.assertEqual(cust_lst.sum(), 0)

    def test_add_func(self):
        add_lst_1 = CustomList([2])
        add_lst_2 = CustomList([2])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([4]))

        add_lst_1 = CustomList([2])
        add_lst_2 = CustomList([])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([2]))

        add_lst_1 = CustomList([])
        add_lst_2 = CustomList([2])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([2]))

        add_lst_1 = CustomList([])
        add_lst_2 = CustomList([])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([]))

        add_lst_1 = CustomList([1, 2, 3, 4])
        add_lst_2 = CustomList([4, 3, 2, 1])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([5, 5, 5, 5]))

        add_lst_1 = CustomList([1, 2, 3, 4])
        add_lst_2 = CustomList([4, 3, 2])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([5, 5, 5, 4]))

        self.assertEqual(add_lst_1, CustomList([1, 2, 3, 4]))
        self.assertEqual(add_lst_2, CustomList([4, 3, 2]))

        add_lst_1 = CustomList([1, 2, 3])
        add_lst_2 = CustomList([4, 3, 2, 1])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([5, 5, 5, 1]))

        self.assertEqual(add_lst_1, CustomList([1, 2, 3]))
        self.assertEqual(add_lst_2, CustomList([4, 3, 2, 1]))

        add_lst_1 = CustomList([1, 2, 3, 4])
        add_lst_2 = CustomList([-4, -3, -2, -1])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([-3, -1, 1, 3]))

    def test_sub_func(self):
        sub_lst_1 = CustomList([2])
        sub_lst_2 = CustomList([2])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([0]))

        sub_lst_1 = CustomList([2])
        sub_lst_2 = CustomList([])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([2]))

        sub_lst_1 = CustomList([])
        sub_lst_2 = CustomList([2])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-2]))

        sub_lst_1 = CustomList([])
        sub_lst_2 = CustomList([])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([]))

        sub_lst_1 = CustomList([1, 2, 3, 4])
        sub_lst_2 = CustomList([4, 3, 2, 1])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-3, -1, 1, 3]))

        sub_lst_1 = CustomList([1, 2, 3, 4])
        sub_lst_2 = CustomList([4, 3, 2])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-3, -1, 1, 4]))

        sub_lst_1 = CustomList([1, 2, 3])
        sub_lst_2 = CustomList([4, 3, 2, 1])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-3, -1, 1, -1]))

        sub_lst_1 = CustomList([1, 2, 3, 4])
        sub_lst_2 = CustomList([-4, -3, -2, -1])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([5, 5, 5, 5]))

    def test_cross_add(self):
        add_lst_1 = CustomList([2])
        add_lst_2 = []
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([2]))

        add_lst_1 = CustomList([])
        add_lst_2 = [2]
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([2]))

        add_lst_1 = CustomList([])
        add_lst_2 = []
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([]))

        add_lst_1 = CustomList([1, 2, 3, 4])
        add_lst_2 = [4, 3, 2, 1]
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([5, 5, 5, 5]))

        add_lst_1 = CustomList([1, 2, 3, 4])
        add_lst_2 = [4, 3, 2]
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([5, 5, 5, 4]))

        self.assertEqual(add_lst_1, CustomList([1, 2, 3, 4]))

        add_lst_1 = CustomList([1, 2, 3])
        add_lst_2 = [4, 3, 2, 1]
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([5, 5, 5, 1]))

        self.assertEqual(add_lst_1, CustomList([1, 2, 3]))

        add_lst_1 = CustomList([1, 2, 3, 4])
        add_lst_2 = [-4, -3, -2, -1]
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([-3, -1, 1, 3]))

        add_lst_1 = [2]
        add_lst_2 = CustomList([2])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([4]))

        add_lst_1 = [2]
        add_lst_2 = CustomList([])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([2]))

        add_lst_1 = []
        add_lst_2 = CustomList([2])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([2]))

        add_lst_1 = []
        add_lst_2 = CustomList([])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([]))

        add_lst_1 = [1, 2, 3, 4]
        add_lst_2 = CustomList([4, 3, 2, 1])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([5, 5, 5, 5]))

        add_lst_1 = [1, 2, 3, 4]
        add_lst_2 = CustomList([4, 3, 2])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([5, 5, 5, 4]))

        self.assertEqual(add_lst_2, CustomList([4, 3, 2]))

        add_lst_1 = [1, 2, 3]
        add_lst_2 = CustomList([4, 3, 2, 1])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([5, 5, 5, 1]))

        self.assertEqual(add_lst_2, CustomList([4, 3, 2, 1]))

        add_lst_1 = [1, 2, 3, 4]
        add_lst_2 = CustomList([-4, -3, -2, -1])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([-3, -1, 1, 3]))

    def test_cross_sub(self):
        sub_lst_1 = CustomList([2])
        sub_lst_2 = []
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([2]))

        sub_lst_1 = CustomList([])
        sub_lst_2 = [2]
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-2]))

        sub_lst_1 = CustomList([])
        sub_lst_2 = []
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([]))

        sub_lst_1 = CustomList([1, 2, 3, 4])
        sub_lst_2 = [4, 3, 2, 1]
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-3, -1, 1, 3]))

        sub_lst_1 = CustomList([1, 2, 3, 4])
        sub_lst_2 = [4, 3, 2]
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-3, -1, 1, 4]))

        self.assertEqual(sub_lst_1, CustomList([1, 2, 3, 4]))

        sub_lst_1 = CustomList([1, 2, 3])
        sub_lst_2 = [4, 3, 2, 1]
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-3, -1, 1, -1]))

        self.assertEqual(sub_lst_1, CustomList([1, 2, 3]))

        sub_lst_1 = CustomList([1, 2, 3, 4])
        sub_lst_2 = [-4, -3, -2, -1]
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([5, 5, 5, 5]))

        sub_lst_1 = [2]
        sub_lst_2 = CustomList([2])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([0]))

        sub_lst_1 = [2]
        sub_lst_2 = CustomList([])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([2]))

        sub_lst_1 = []
        sub_lst_2 = CustomList([2])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-2]))

        sub_lst_1 = []
        sub_lst_2 = CustomList([])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([]))

        sub_lst_1 = [1, 2, 3, 4]
        sub_lst_2 = CustomList([4, 3, 2, 1])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-3, -1, 1, 3]))

        sub_lst_1 = [1, 2, 3, 4]
        sub_lst_2 = CustomList([4, 3, 2])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-3, -1, 1, 4]))

        self.assertEqual(sub_lst_2, CustomList([4, 3, 2]))

        sub_lst_1 = [1, 2, 3]
        sub_lst_2 = CustomList([4, 3, 2, 1])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-3, -1, 1, -1]))

        self.assertEqual(sub_lst_2, CustomList([4, 3, 2, 1]))

        sub_lst_1 = [1, 2, 3, 4]
        sub_lst_2 = CustomList([-4, -3, -2, -1])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([5, 5, 5, 5]))

    def test_logical_operations(self):
        self.assertTrue(CustomList([]) == CustomList([]))
        self.assertTrue(CustomList([]) >= CustomList([]))
        self.assertTrue(CustomList([]) <= CustomList([]))
        self.assertFalse(CustomList([]) < CustomList([]))
        self.assertFalse(CustomList([]) > CustomList([]))
        self.assertFalse(CustomList([]) != CustomList([]))

        self.assertTrue(CustomList([3]) != CustomList([2]))
        self.assertTrue(CustomList([3]) >= CustomList([2]))
        self.assertTrue(CustomList([3]) > CustomList([2]))
        self.assertFalse(CustomList([3]) < CustomList([2]))
        self.assertFalse(CustomList([3]) <= CustomList([2]))
        self.assertFalse(CustomList([3]) == CustomList([2]))

        self.assertTrue(CustomList([3]) != CustomList([0]))
        self.assertTrue(CustomList([3]) >= CustomList([0]))
        self.assertTrue(CustomList([3]) > CustomList([0]))
        self.assertFalse(CustomList([3]) < CustomList([0]))
        self.assertFalse(CustomList([3]) <= CustomList([0]))
        self.assertFalse(CustomList([3]) == CustomList([0]))

        self.assertTrue(CustomList([3]) == CustomList([3]))
        self.assertTrue(CustomList([3]) >= CustomList([3]))
        self.assertTrue(CustomList([3]) <= CustomList([3]))
        self.assertFalse(CustomList([3]) < CustomList([3]))
        self.assertFalse(CustomList([3]) > CustomList([3]))
        self.assertFalse(CustomList([3]) != CustomList([3]))

        self.assertTrue(CustomList([3, 8]) != CustomList([9]))
        self.assertTrue(CustomList([3, 8]) >= CustomList([9]))
        self.assertTrue(CustomList([3, 8]) > CustomList([9]))
        self.assertFalse(CustomList([3, 8]) < CustomList([9]))
        self.assertFalse(CustomList([3, 8]) <= CustomList([9]))
        self.assertFalse(CustomList([3, 8]) == CustomList([9]))

    def test_print(self):
        self.assertEqual(CustomList([1, 2, 3]).__str__(), "[1, 2, 3], sum: 6")
        self.assertEqual(CustomList([]).__str__(), "[], sum: 0")


if __name__ == '__main__':
    unittest.main()
