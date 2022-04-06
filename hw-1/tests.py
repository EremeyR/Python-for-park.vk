import unittest
import TickTack


class TestStringMethods(unittest.TestCase):
    game = TickTack.TicTacGame()

    def test_validate_input(self):
        self.assertTrue(self.game.validate_input("3"))          # correct input
        self.assertFalse(self.game.validate_input("-3"))        # incorrect int
        self.assertFalse(self.game.validate_input("42"))        # too big int
        self.assertFalse(self.game.validate_input("4.2"))       # bool
        self.assertFalse(self.game.validate_input("v"))         # incorrect str
        self.assertFalse(self.game.validate_input("value"))     # incorrect str

        for i in range(9):                                      # correct
            self.assertTrue(self.game.validate_input(i))

        for i in range(9):                                      # correct
            self.assertTrue(self.game.validate_input(str(i)))

        self.assertFalse(self.game.validate_input("-1"))
        self.assertFalse(self.game.validate_input("9"))

        for i in range(9):                                      # correct
            self.game.set_sell(i)

        for i in range(9):                                      # double entry
            self.assertFalse(self.game.validate_input(str(i)))

        self.game.reset()

    def test_horizontal_check_winner(self):
        for i in range(2):  # horizontal filling
            self.game.set_sell(i)
            self.assertFalse(self.game.check_winner())
            self.game.set_sell(i + 3)
            self.assertFalse(self.game.check_winner())

        self.game.set_sell(2)
        self.assertTrue(self.game.check_winner())

        self.game.reset()

    def test_vertical_check_winner(self):
        for i in range(2):  # vertical filling
            self.game.set_sell(i * 3)
            self.assertFalse(self.game.check_winner())
            self.game.set_sell(i * 3 + 1)
            self.assertFalse(self.game.check_winner())

        self.game.set_sell(8)
        self.assertFalse(self.game.check_winner())
        self.game.set_sell(7)
        self.assertTrue(self.game.check_winner())

        self.game.reset()

    def test_vertical_check_winner_incorrect(self):
        self.game.set_sell(8)
        for i in range(2):  # vertical filling
            self.game.set_sell(i * 3)

            if self.game.validate_input(i * 42):
                self.game.set_sell(int(i * 42))

            self.assertFalse(self.game.check_winner())
            self.game.set_sell(i * 3 + 1)

            if self.game.validate_input("i * 3 + 1"):
                self.game.set_sell(int("i * 3 + 1"))

            self.assertFalse(self.game.check_winner())

        if self.game.validate_input(-100):
            self.game.set_sell(int(-100))
        self.game.set_sell(6)
        self.assertTrue(self.game.check_winner())
        self.game.reset()

    def test_main_diagonal_check_winner(self):
        for i in range(0, 8, 4):    # diagonal filling
            self.game.set_sell(i)
            self.assertFalse(self.game.check_winner())
            self.game.set_sell(i + 1)
            self.assertFalse(self.game.check_winner())

        self.game.set_sell(8)
        self.assertTrue(self.game.check_winner())

        self.game.reset()

    def test_minor_diagonal_check_winner(self):
        for i in range(2, 6, 2):    # diagonal filling
            self.assertFalse(self.game.check_winner())
            self.game.set_sell(i - 1)
            self.assertFalse(self.game.check_winner())
            self.game.set_sell(i)

        self.game.set_sell(0)
        self.assertFalse(self.game.check_winner())
        self.game.set_sell(6)
        self.assertTrue(self.game.check_winner())

        self.game.reset()

    def test_drawn_check(self):
        for i in range(5):    # diagonal filling
            self.assertFalse(self.game.check_winner())
            self.game.set_sell(i)

        for i in range(8, 4, -1):    # diagonal filling
            self.assertFalse(self.game.check_winner())
            self.game.set_sell(i)

        self.assertFalse(self.game.check_winner())
        self.assertTrue(self.game.check_drawn())

        self.game.reset()


if __name__ == '__main__':
    unittest.main()
