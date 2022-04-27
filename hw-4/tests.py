import implementation as impt

import unittest


class CustomClass(metaclass=impt.CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


class Data:
    num = impt.Integer()
    name = impt.String()
    price = impt.PositiveInteger()


class TestStringMethods(unittest.TestCase):
    def test_metaclass(self):
        inst = CustomClass()

        self.assertTrue(hasattr(CustomClass, "custom_x"))
        self.assertTrue(hasattr(inst, "custom_x"))
        self.assertEqual(inst.custom_x, 50)
        self.assertFalse(hasattr(inst, "x"))

        self.assertTrue(hasattr(inst, "custom_line"))
        self.assertEqual(inst.custom_line(), 100)
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

        try:
            data.num
            self.fail()
        except UnboundLocalError:
            pass

        try:
            data.name
            self.fail()
        except UnboundLocalError:
            pass

        try:
            data.price
            self.fail()
        except UnboundLocalError:
            pass

        data.num = 42
        self.assertEqual(data.num, 42)

        data.num = -42
        self.assertEqual(data.num, -42)

        try:
            data.num = 4.2
            self.fail()
        except ValueError:
            pass

        try:
            data.num = "42"
            self.fail()
        except ValueError:
            pass

        data.price = 42
        self.assertEqual(data.price, 42)

        try:
            data.price = -42
            self.fail()
        except ValueError:
            pass

        try:
            data.price = 4.2
            self.fail()
        except ValueError:
            pass

        try:
            data.price = "42"
            self.fail()
        except ValueError:
            pass

        data.name = "Name"
        self.assertEqual(data.name, "Name")

        data.name = "42"
        self.assertEqual(data.name, "42")

        try:
            data.name = 42
            self.fail()
        except ValueError:
            pass


if __name__ == '__main__':
    unittest.main()
