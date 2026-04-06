import unittest
from main import TicTacToeBuggy

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        """Виконується перед кожним тестом"""
        self.game = TicTacToeBuggy()

    def test_initial_state(self):
        """Перевірка початкового стану"""
        self.assertEqual(self.game.current_player, "X")
        self.assertIn(" ", self.game.board)

    def test_player_switch(self):
        """Перевірка зміни гравця після ходу"""
        self.game.make_move(0) # X робить хід
        self.assertEqual(self.game.current_player, "O")
        self.game.make_move(1) # O робить хід
        self.assertEqual(self.game.current_player, "X")

    def test_winner_detection(self):
        """Перевірка логіки перемоги (горизонталь)"""
        self.game.board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        self.assertTrue(self.game.check_winner())

if __name__ == "__main__":
    unittest.main()