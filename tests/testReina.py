import unittest
from chess.queen import Queen
from chess.board import Board
from unittest.mock import MagicMock

class TestQueenValidPositions(unittest.TestCase):

# Simbolos piezas reinas (blanco y negro)

    def test_queen_symbol_white(self):
        board = Board()
        queen = Queen("WHITE", board)
        self.assertEqual(queen.symbol(), '♕')

    def test_queen_symbol_black(self):
        board = Board()
        queen = Queen("BLACK", board)
        self.assertEqual(queen.symbol(), '♛')


    def setUp(self):
        self.board = MagicMock()  # Simulamos el tablero
        self.white_queen = Queen("WHITE", self.board)  # Instancia de la reina blanca

    def test_valid_move_vertical(self):
        move = {'from_row': 3, 'from_col': 3, 'to_row': 5, 'to_col': 3}
        self.white_queen.find_valid_moves = MagicMock(return_value=[(5, 3), (4, 3)])
        self.assertTrue(self.white_queen.queen_valid_positions(move))  # Debe ser verdadero

    def test_valid_move_horizontal(self):
        move = {'from_row': 3, 'from_col': 3, 'to_row': 3, 'to_col': 5}
        self.white_queen.find_valid_moves = MagicMock(return_value=[(3, 5), (3, 4)])
        self.assertTrue(self.white_queen.queen_valid_positions(move))  # Debe ser verdadero

    def test_valid_move_diagonal(self):
        move = {'from_row': 3, 'from_col': 3, 'to_row': 5, 'to_col': 5}
        self.white_queen.find_valid_moves = MagicMock(return_value=[(5, 5), (4, 4)])
        self.assertTrue(self.white_queen.queen_valid_positions(move))  # Debe ser verdadero

    def test_invalid_move(self):
        move = {'from_row': 3, 'from_col': 3, 'to_row': 5, 'to_col': 4}
        self.white_queen.find_valid_moves = MagicMock(return_value=[(5, 5), (4, 4)])
        self.assertFalse(self.white_queen.queen_valid_positions(move))  # Debe ser falso


if __name__ == "__main__":
    unittest.main()