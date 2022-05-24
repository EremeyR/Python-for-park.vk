"""
Part 1
"""


class CustomMeta(type):
    """
    Adds "custom_" to all attributes of the class
    """
    def __setattr__(cls, name, value):
        cls.__dict__[f"custom_{name}"] = value

    def __new__(cls, clsname, bases, attrs):
        custom_attrs = {}

        for attr, value in attrs.items():
            if attr.startswith("__") and attr.endswith("__"):
                custom_attrs[attr] = value
            else:
                custom_attrs[f"custom_{attr}"] = value

        custom_attrs["__setattr__"] = CustomMeta.__setattr__
        return super().__new__(cls, clsname, bases, custom_attrs)

# Part 2


class Integer:
    """
    int descriptor
    """
    def __init__(self):
        self.i = None

    def __str__(self):
        return "Custom_by_metaclass"

    def __set__(self, obj, val):
        if not isinstance(val, int):
            raise ValueError("not int")

        self.i = val

    def __get__(self, obj, objtype):
        if not self.i:
            raise UnboundLocalError("empty value")

        return self.i


class String:
    """
        str descriptor
    """
    def __init__(self):
        self.strg = None

    def __set__(self, obj, val):
        if not isinstance(val, str):
            raise ValueError("not string")

        self.strg = val

    def __get__(self, obj, objtype):
        if not self.strg:
            raise UnboundLocalError("empty value")

        return self.strg


class PositiveInteger:
    """
            positive int descriptor
    """
    def __init__(self):
        self.i = None

    def __set__(self, obj, val):
        if not isinstance(val, int):
            raise ValueError("not int")
        if val < 0:
            raise ValueError("not positive int")

        self.i = val

    def __get__(self, obj, objtype):
        if not self.i:
            raise UnboundLocalError("empty value")

        return self.i
