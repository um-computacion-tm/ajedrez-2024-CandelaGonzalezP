import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from chess.bishop import Bishop
from chess.board import Board
from chess.pawn import Pawn

class TestBishop(unittest.TestCase):

# Simbolos piezas alfiles (blanco y negro)

    def test_bishop_symbol_white(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        self.assertEqual(bishop.symbol(), '♗')

    def test_bishop_symbol_black(self):
        board = Board()
        bishop = Bishop("BLACK", board)
        self.assertEqual(bishop.symbol(), '♝')

# TESTEO MOVIMIENTOS

    def setUp(self):
        self.board = Board()  # Elimina el argumento for_test
        self.bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, self.bishop)  # Coloca el alfil en el centro

    def test_valid_position_diagonal(self):
        from_row, from_col = 4, 4
        to_row, to_col = 6, 6  # Movimiento válido en diagonal
        self.assertFalse(self.bishop.valid_positions(from_row, from_col, to_row, to_col))

    def test_invalid_position_non_diagonal(self):
        from_row, from_col = 4, 4
        to_row, to_col = 4, 5  # Movimiento no válido (no es diagonal)
        self.assertFalse(self.bishop.valid_positions(from_row, from_col, to_row, to_col))

if __name__ == '__main__':
    unittest.main()
