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

        self.game.set_sell(3)
        self.assertFalse(self.game.validate_input("3"))         # double entry

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

    def test_main_diagonal_check_winner(self):
        for i in range(0, 8, 4):    # diagonal filling
            self.game.set_sell(i)
            self.assertFalse(self.game.check_winner())
            self.game.set_sell(i + 1)
            self.assertFalse(self.game.check_winner())

        self.game.set_sell(8)
        self.assertTrue(self.game.check_winner())

        self.game.reset()

    def test_drawn_check(self):
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

    def test_minor_diagonal_check_winner(self):
        for i in range(5):  # filling without winner
            self.game.set_sell(i)
        self.game.set_sell(8)
        self.game.set_sell(5)
        self.game.set_sell(6)
        self.assertFalse(self.game.check_winner())
        self.game.set_sell(7)
        self.assertTrue(self.game.check_winner())

        self.game.reset()


if __name__ == '__main__':
    unittest.main()
