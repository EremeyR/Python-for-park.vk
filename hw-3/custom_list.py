def fill_zeros(other, difference: int):
    for _ in range(difference):
        other.append(0)


class CustomList(list):
    def __add__(self, other):
        return self.__operate(other, lambda x, y: x + y)

    def __sub__(self, other):
        return self.__operate(other, lambda x, y: x - y)

    def __radd__(self, other):
        return self.__add__(other)

    def __rsub__(self, other):
        return self.__operate(other, lambda x, y: y - x)

    def __operate(self, other: list, operation):
        this = self.copy()
        other = other.copy()
        difference = self.__len__() - len(other)
        if difference > 0:
            fill_zeros(other, difference)
        elif difference < 0:
            fill_zeros(this, abs(difference))

        temp_lst = []
        for i, value in enumerate(this):
            temp_lst.append(operation(value, other[i]))

        return CustomList(temp_lst)

    def sum(self) -> int:
        result = 0
        for value in self:
            result += value

        return result

    def __str__(self):
        return f"{super().__str__()}, sum: {self.sum()}"

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
