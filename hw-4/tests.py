import unittest

import implementation as impt


class CustomClass(metaclass=impt.CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return len(self.__str__())

    def __str__(self):
        return "Custom_by_metaclass"


class Data:
    __num = impt.Integer()
    __name = impt.String()
    __price = impt.PositiveInteger()

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        self.__num = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value


class TestStringMethods(unittest.TestCase):
    def test_metaclass(self):
        inst = CustomClass()

        self.assertTrue(hasattr(CustomClass, "custom_x"))
        self.assertTrue(hasattr(inst, "custom_x"))
        self.assertEqual(inst.custom_x, 50)
        self.assertFalse(hasattr(inst, "x"))

        self.assertTrue(hasattr(inst, "custom_line"))
        self.assertEqual(inst.custom_line(), len("Custom_by_metaclass"))
        self.assertFalse(hasattr(inst, "line"))

        self.assertTrue(hasattr(inst, "custom_val"))
        self.assertEqual(inst.custom_val, 99)
        self.assertFalse(hasattr(inst, "val"))

        self.assertEqual(str(inst), "Custom_by_metaclass")

        inst.dynamic = "added later"

        self.assertFalse(hasattr(CustomClass, "custom_dynamic"))
        self.assertTrue(hasattr(inst, "custom_dynamic"))
        self.assertEqual(inst.custom_dynamic, "added later")
        self.assertFalse(hasattr(inst, "dynamic"))

        self.assertFalse(hasattr(inst, "yyy"))

    def test_descriptors(self):
        data = Data()

        with self.assertRaises(UnboundLocalError):
            _ = data.num

        with self.assertRaises(UnboundLocalError):
            _ = data.name

        with self.assertRaises(UnboundLocalError):
            _ = data.price

        data.num = 42
        self.assertEqual(data.num, 42)

        data.num = -42
        self.assertEqual(data.num, -42)

        with self.assertRaises(ValueError):
            data.num = 4.2

        with self.assertRaises(ValueError):
            data.num = "42"

        self.assertEqual(data.num, -42)

        data.price = 42
        self.assertEqual(data.price, 42)

        with self.assertRaises(ValueError):
            data.price = -42

        with self.assertRaises(ValueError):
            data.price = 4.2

        with self.assertRaises(ValueError):
            data.price = "42"

        self.assertEqual(data.price, 42)

        data.name = "Name"
        self.assertEqual(data.name, "Name")

        data.name = "42"
        self.assertEqual(data.name, "42")

        with self.assertRaises(ValueError):
            data.name = 42

        self.assertEqual(data.name, "42")


if __name__ == '__main__':
    unittest.main()
