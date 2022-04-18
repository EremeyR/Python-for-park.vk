def fill_zeros(other: list, difference: int):
    for _ in range(difference):
        other.append(0)


def remove_zeros(other: list, difference: int):
    for _ in range(difference):
        other.pop(-1)


class CustomList(list):
    def __init__(self, lst=None) -> None:
        super().__init__()
        if not lst:
            self.__values = []
        else:
            self.__values = lst

    def __getitem__(self, item):
        return self.__values[item]

    def __add__(self, other):
        return self.__calculate(other, lambda x, y: x + y)

    def __sub__(self, other):
        return self.__calculate(other, lambda x, y: x - y)

    def __calculate(self, other, operation):
        if isinstance(other, CustomList):
            return self.__operate(other.to_py_list, operation)
        if isinstance(other, list):
            return self.__operate(other, operation)

        raise Exception("incorrect type")

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__calculate(other, lambda x, y: y - x)

    def __operate(self, other: list, operation):
        difference = len(self.__values) - len(other)
        if difference > 0:
            fill_zeros(other, difference)
        elif difference < 0:
            fill_zeros(self.__values, abs(difference))

        temp_lst = []
        for i, value in enumerate(self.__values):
            temp_lst.append(operation(value, other[i]))

        if difference > 0:
            remove_zeros(other, difference)
        elif difference < 0:
            remove_zeros(self.__values, abs(difference))
        return CustomList(temp_lst)

    def sum(self) -> int:
        result = 0
        for value in self.__values:
            result += value

        return result

    def __str__(self):
        return f"{str(self.__values)}, sum: {self.sum()}"

    def __lt__(self, other):
        return self.sum() < other.sum()

    def __le__(self, other):
        return self.sum() <= other.sum()

    def __eq__(self, other):
        return self.sum() == other.sum()

    def __ne__(self, other):
        return self.sum() != other.sum()

    def __gt__(self, other):
        return self.sum() > other.sum()

    def __ge__(self, other):
        return self.sum() >= other.sum()

    @property
    def to_py_list(self):
        return self.__values
