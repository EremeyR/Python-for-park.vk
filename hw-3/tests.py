import unittest
from custom_list import CustomList


def is_equal(l_list, r_list):
    if len(l_list) != len(r_list):
        return False

    for i, l_list_cell in enumerate(l_list):
        if l_list_cell != r_list[i]:
            return False
    return True


class TestStringMethods(unittest.TestCase):
    def test_sum_func(self):
        cust_lst = CustomList([1])
        self.assertEqual(cust_lst.sum(), 1)
        self.assertTrue(is_equal(cust_lst, CustomList([1])))

        cust_lst = CustomList([1, 2, 3])
        self.assertEqual(cust_lst.sum(), 6)
        self.assertTrue(is_equal(cust_lst, CustomList([1, 2, 3])))

        cust_lst = CustomList([-1])
        self.assertEqual(cust_lst.sum(), -1)

        cust_lst = CustomList([-40, -2])
        self.assertEqual(cust_lst.sum(), -42)

        cust_lst = CustomList([-50, 8])
        self.assertEqual(cust_lst.sum(), -42)

        cust_lst = CustomList([])
        self.assertEqual(cust_lst.sum(), 0)
        self.assertTrue(is_equal(cust_lst, CustomList([])))

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
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([2])))
        self.assertTrue(is_equal(add_lst_2, CustomList([2])))

        add_lst_1 = CustomList([2])
        add_lst_2 = CustomList([])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([2]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([2])))
        self.assertTrue(is_equal(add_lst_2, CustomList([])))

        add_lst_1 = CustomList([])
        add_lst_2 = CustomList([2])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([2]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([])))
        self.assertTrue(is_equal(add_lst_2, CustomList([2])))

        add_lst_1 = CustomList([])
        add_lst_2 = CustomList([])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([])))
        self.assertTrue(is_equal(add_lst_2, CustomList([])))

        add_lst_1 = CustomList([1, 2, 3, 4])
        add_lst_2 = CustomList([4, 3, 2])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([5, 5, 5, 4]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([1, 2, 3, 4])))
        self.assertTrue(is_equal(add_lst_2, CustomList([4, 3, 2])))

        self.assertEqual(add_lst_1, CustomList([1, 2, 3, 4]))
        self.assertEqual(add_lst_2, CustomList([4, 3, 2]))

        add_lst_1 = CustomList([1, 2, 3])
        add_lst_2 = CustomList([4, 3, 2, 1])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([5, 5, 5, 1]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([1, 2, 3])))
        self.assertTrue(is_equal(add_lst_2, CustomList([4, 3, 2, 1])))

        self.assertEqual(add_lst_1, CustomList([1, 2, 3]))
        self.assertEqual(add_lst_2, CustomList([4, 3, 2, 1]))

        add_lst_1 = CustomList([1, 2, 3, 4])
        add_lst_2 = CustomList([-4, -3, -2, -1])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([-3, -1, 1, 3]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([1, 2, 3, 4])))
        self.assertTrue(is_equal(add_lst_2, CustomList([-4, -3, -2, -1])))

    def test_sub_func(self):
        sub_lst_1 = CustomList([2])
        sub_lst_2 = CustomList([2])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([0]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([2])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([2])))

        sub_lst_1 = CustomList([2])
        sub_lst_2 = CustomList([])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([2]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([2])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([])))

        sub_lst_1 = CustomList([])
        sub_lst_2 = CustomList([2])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-2]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([2])))

        sub_lst_1 = CustomList([])
        sub_lst_2 = CustomList([])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([])))

        sub_lst_1 = CustomList([1, 2, 3, 4])
        sub_lst_2 = CustomList([4, 3, 2, 1])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-3, -1, 1, 3]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([1, 2, 3, 4])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([4, 3, 2, 1])))

        sub_lst_1 = CustomList([1, 2, 3, 4])
        sub_lst_2 = CustomList([4, 3, 2])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-3, -1, 1, 4]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([1, 2, 3, 4])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([4, 3, 2])))

        sub_lst_1 = CustomList([1, 2, 3])
        sub_lst_2 = CustomList([4, 3, 2, 1])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-3, -1, 1, -1]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([1, 2, 3])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([4, 3, 2, 1])))

        sub_lst_1 = CustomList([1, 2, 3, 4])
        sub_lst_2 = CustomList([-4, -3, -2, -1])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([5, 5, 5, 5]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([1, 2, 3, 4])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([-4, -3, -2, -1])))

    def test_cross_add(self):
        add_lst_1 = CustomList([2])
        add_lst_2 = []
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([2]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([2])))
        self.assertTrue(is_equal(add_lst_2, CustomList([])))

        add_lst_1 = CustomList([])
        add_lst_2 = [2]
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([2]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([])))
        self.assertTrue(is_equal(add_lst_2, CustomList([2])))

        add_lst_1 = CustomList([])
        add_lst_2 = []
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([])))
        self.assertTrue(is_equal(add_lst_2, CustomList([])))

        add_lst_1 = CustomList([1, 2, 3, 4])
        add_lst_2 = [4, 3, 2, 1]
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([5, 5, 5, 5]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([1, 2, 3, 4])))
        self.assertTrue(is_equal(add_lst_2, CustomList([4, 3, 2, 1])))

        add_lst_1 = CustomList([1, 2, 3, 4])
        add_lst_2 = [4, 3, 2]
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([5, 5, 5, 4]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([1, 2, 3, 4])))
        self.assertTrue(is_equal(add_lst_2, CustomList([4, 3, 2])))

        self.assertEqual(add_lst_1, CustomList([1, 2, 3, 4]))

        add_lst_1 = CustomList([1, 2, 3])
        add_lst_2 = [4, 3, 2, 1]
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([5, 5, 5, 1]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([1, 2, 3])))
        self.assertTrue(is_equal(add_lst_2, CustomList([4, 3, 2, 1])))

        self.assertEqual(add_lst_1, CustomList([1, 2, 3]))

        add_lst_1 = CustomList([1, 2, 3, 4])
        add_lst_2 = [-4, -3, -2, -1]
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([-3, -1, 1, 3]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([1, 2, 3, 4])))
        self.assertTrue(is_equal(add_lst_2, CustomList([-4, -3, -2, -1])))

    def test_cross_add_second_pos(self):
        add_lst_1 = [2]
        add_lst_2 = CustomList([2])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([4]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([2])))
        self.assertTrue(is_equal(add_lst_2, CustomList([2])))

        add_lst_1 = [2]
        add_lst_2 = CustomList([])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([2]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([2])))
        self.assertTrue(is_equal(add_lst_2, CustomList([])))

        add_lst_1 = []
        add_lst_2 = CustomList([2])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([2]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([])))
        self.assertTrue(is_equal(add_lst_2, CustomList([2])))

        add_lst_1 = []
        add_lst_2 = CustomList([])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([])))
        self.assertTrue(is_equal(add_lst_2, CustomList([])))

        add_lst_1 = [1, 2, 3, 4]
        add_lst_2 = CustomList([4, 3, 2])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([5, 5, 5, 4]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([1, 2, 3, 4])))
        self.assertTrue(is_equal(add_lst_2, CustomList([4, 3, 2])))

        self.assertEqual(add_lst_2, CustomList([4, 3, 2]))

        add_lst_1 = [1, 2, 3]
        add_lst_2 = CustomList([4, 3, 2, 1])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([5, 5, 5, 1]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([1, 2, 3])))
        self.assertTrue(is_equal(add_lst_2, CustomList([4, 3, 2, 1])))

        self.assertEqual(add_lst_2, CustomList([4, 3, 2, 1]))

        add_lst_1 = [1, 2, 3, 4]
        add_lst_2 = CustomList([-4, -3, -2, -1])
        self.assertEqual(add_lst_1 + add_lst_2, CustomList([-3, -1, 1, 3]))
        self.assertTrue(isinstance(add_lst_1 + add_lst_2, CustomList))
        self.assertTrue(is_equal(add_lst_1, CustomList([1, 2, 3, 4])))
        self.assertTrue(is_equal(add_lst_2, CustomList([-4, -3, -2, -1])))

    def test_cross_sub(self):
        sub_lst_1 = CustomList([2])
        sub_lst_2 = []
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([2]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([2])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([])))

        sub_lst_1 = CustomList([])
        sub_lst_2 = [2]
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-2]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([2])))

        sub_lst_1 = CustomList([])
        sub_lst_2 = []
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([])))

        sub_lst_1 = CustomList([1, 2, 3, 4])
        sub_lst_2 = [4, 3, 2, 1]
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-3, -1, 1, 3]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([1, 2, 3, 4])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([4, 3, 2, 1])))

        sub_lst_1 = CustomList([1, 2, 3, 4])
        sub_lst_2 = [4, 3, 2]
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-3, -1, 1, 4]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([1, 2, 3, 4])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([4, 3, 2])))

        self.assertEqual(sub_lst_1, CustomList([1, 2, 3, 4]))

        sub_lst_1 = CustomList([1, 2, 3])
        sub_lst_2 = [4, 3, 2, 1]
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-3, -1, 1, -1]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([1, 2, 3])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([4, 3, 2, 1])))

        self.assertEqual(sub_lst_1, CustomList([1, 2, 3]))

        sub_lst_1 = CustomList([1, 2, 3, 4])
        sub_lst_2 = [-4, -3, -2, -1]
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([5, 5, 5, 5]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([1, 2, 3, 4])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([-4, -3, -2, -1])))

    def test_cross_sub_second_pos(self):
        sub_lst_1 = [2]
        sub_lst_2 = CustomList([2])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([0]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([2])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([2])))

        sub_lst_1 = [2]
        sub_lst_2 = CustomList([])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([2]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([2])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([])))

        sub_lst_1 = []
        sub_lst_2 = CustomList([2])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-2]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([2])))

        sub_lst_1 = []
        sub_lst_2 = CustomList([])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([])))

        sub_lst_1 = [1, 2, 3, 4]
        sub_lst_2 = CustomList([4, 3, 2])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-3, -1, 1, 4]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([1, 2, 3, 4])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([4, 3, 2])))

        self.assertEqual(sub_lst_2, CustomList([4, 3, 2]))

        sub_lst_1 = [1, 2, 3]
        sub_lst_2 = CustomList([4, 3, 2, 1])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([-3, -1, 1, -1]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([1, 2, 3])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([4, 3, 2, 1])))

        self.assertEqual(sub_lst_2, CustomList([4, 3, 2, 1]))

        sub_lst_1 = [1, 2, 3, 4]
        sub_lst_2 = CustomList([-4, -3, -2, -1])
        self.assertEqual(sub_lst_1 - sub_lst_2, CustomList([5, 5, 5, 5]))
        self.assertTrue(isinstance(sub_lst_1 - sub_lst_2, CustomList))
        self.assertTrue(is_equal(sub_lst_1, CustomList([1, 2, 3, 4])))
        self.assertTrue(is_equal(sub_lst_2, CustomList([-4, -3, -2, -1])))

    def test_with_appends(self):
        lst_1 = CustomList([])
        lst_1.append(2)
        lst_2 = []
        self.assertEqual(lst_1 - lst_2, CustomList([2]))
        self.assertTrue(isinstance(lst_1 - lst_2, CustomList))
        self.assertTrue(is_equal(lst_1, CustomList([2])))
        self.assertTrue(is_equal(lst_2, CustomList([])))

        lst_2.append(3)
        lst_2.append(8)
        self.assertEqual(lst_1 - lst_2, CustomList([-1, -8]))
        self.assertEqual(lst_2 - lst_1, CustomList([1, 8]))
        self.assertTrue(isinstance(lst_1 - lst_2, CustomList))
        self.assertTrue(isinstance(lst_2 - lst_1, CustomList))
        self.assertTrue(is_equal(lst_1, CustomList([2])))
        self.assertTrue(is_equal(lst_2, CustomList([3, 8])))

        lst_1.append(-8)
        self.assertEqual(lst_1 + lst_2, CustomList([5, 0]))
        self.assertTrue(isinstance(lst_1 + lst_2, CustomList))
        lst_1.append(-8)
        self.assertEqual(lst_2 + lst_1, CustomList([5, 0, -8]))
        self.assertTrue(isinstance(lst_2 + lst_1, CustomList))
        self.assertTrue(is_equal(lst_1, CustomList([2, -8, -8])))
        self.assertTrue(is_equal(lst_2, CustomList([3, 8])))

    def test_logical_operations(self):
        self.assertTrue(CustomList([]) >= CustomList([]))
        self.assertTrue(CustomList([]) <= CustomList([]))
        self.assertFalse(CustomList([]) < CustomList([]))
        self.assertFalse(CustomList([]) > CustomList([]))
        self.assertFalse(CustomList([]) != CustomList([]))
        self.assertTrue(is_equal(CustomList([]), CustomList([])))

        self.assertTrue(CustomList([3]) != CustomList([2]))
        self.assertTrue(CustomList([3]) >= CustomList([2]))
        self.assertTrue(CustomList([3]) > CustomList([2]))
        self.assertFalse(CustomList([3]) < CustomList([2]))
        self.assertFalse(CustomList([3]) <= CustomList([2]))
        self.assertFalse(is_equal(CustomList([3]), CustomList([2])))

        self.assertTrue(CustomList([3]) != CustomList([0]))
        self.assertTrue(CustomList([3]) >= CustomList([0]))
        self.assertTrue(CustomList([3]) > CustomList([0]))
        self.assertFalse(CustomList([3]) < CustomList([0]))
        self.assertFalse(CustomList([3]) <= CustomList([0]))
        self.assertFalse(is_equal(CustomList([3]), CustomList([0])))

        self.assertTrue(CustomList([3]) >= CustomList([3]))
        self.assertTrue(CustomList([3]) <= CustomList([3]))
        self.assertFalse(CustomList([3]) < CustomList([3]))
        self.assertFalse(CustomList([3]) > CustomList([3]))
        self.assertFalse(CustomList([3]) != CustomList([3]))
        self.assertTrue(is_equal(CustomList([3]), CustomList([3])))

        self.assertTrue(CustomList([3, 8]) != CustomList([9]))
        self.assertTrue(CustomList([3, 8]) >= CustomList([9]))
        self.assertTrue(CustomList([3, 8]) > CustomList([9]))
        self.assertFalse(CustomList([3, 8]) < CustomList([9]))
        self.assertFalse(CustomList([3, 8]) <= CustomList([9]))
        self.assertFalse(is_equal(CustomList([3, 8]), CustomList([9])))

    def test_print(self):
        self.assertEqual(CustomList([1, 2, 3]).__str__(), "[1, 2, 3], sum: 6")
        self.assertEqual(CustomList([]).__str__(), "[], sum: 0")

    def test_equal(self):
        self.assertFalse(CustomList([3]) == CustomList([]))
        self.assertFalse(CustomList([3]) == CustomList([2]))
        self.assertFalse(CustomList([3]) == CustomList([3, 1]))
        self.assertTrue(CustomList([3]) == CustomList([3]))
        self.assertTrue(CustomList([]) == CustomList([]))
        self.assertTrue(CustomList([3]) == CustomList([1, 2]))


if __name__ == '__main__':
    unittest.main()
