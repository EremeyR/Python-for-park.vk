class TicTacGame:

    def start_game(self):
        while not (self.check_winner() or self.check_drawn()):
            self.show()
            current_cell = input()
            if self.validate_input(current_cell):
                self.set_sell(int(current_cell))

        self.show(False)

    def show(self, is_game=True):
        print(self.__message, end="")

        if is_game:
            print(f"\nTurn {self.__counter}. "
                  f"Please, enter {self.__current_tag} position")

        for i in range(3):
            print('\n|', end="")
            for j in range(3):
                print(self.__field[i * 3 + j], '|', end="", sep="")

        if is_game:
            print('\n\n> ', end="")

    def validate_input(self, value) -> bool:
        if not str(value).isdigit():
            self.__message = "Incorrect input: you must enter a digit\n"
            return False

        if 8 < int(value) or int(value) < 0:
            self.__message = "Incorrect input: you must " \
                             "enter a digit from the range [0, 8]\n"
            return False

        if self.__field[int(value)] != ' ':
            self.__message = "Incorrect input: you must chose free cell\n"
            return False

        return True

    def set_sell(self, cell_number):
        self.__field[cell_number] = self.__current_tag
        self.__counter += 1
        self.__change_mark()

    def check_winner(self) -> bool:
        # checking horizontals
        for i in range(3):
            if self.__check_line(range(i * 3, i * 3 + 3)):
                return True

        # checking verticals
        for i in range(3):
            if self.__check_line(range(i, i + 7, 3)):
                return True

        # checking main diagonal
        _diag = [0, 4, 8]
        if self.__check_line(range(0, 9, 4)):
            return True

        # checking minor diagonal
        if self.__check_line(range(2, 7, 2)):
            return True

        return False

    def check_drawn(self) -> bool:
        if self.__counter == 10:
            self.__message = "\nThe game is drawn\n"
            return True
        return False

    def __change_mark(self):
        self.__current_tag = '0' if self.__current_tag == 'X' else 'X'

    def __check_line(self, line) -> bool:
        last_tag = self.__field[line[0]]
        similar_tags = 1

        for i in line[1:]:
            if last_tag == self.__field[i] and last_tag != " ":
                similar_tags += 1
                last_tag = self.__field[i]

        if similar_tags == 3:
            self.__message = f"\n{self.__field[line[0]]}-player's won." \
                             f" Congratulations!\n"
            return True

        return False

    def reset(self):
        self.__field = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.__current_tag = 'X'
        self.__counter = 1
        self.__message = ""

    __field = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    __current_tag = 'X'
    __counter = 1
    __message = ""


if __name__ == "__main__":
    game = TicTacGame()
    while True:
        game.start_game()
        game.reset()
        print("\n\nNEW GAME!")
