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

# Inicia tablero
    def setUp(self):
        self.board = Board(for_test=True)
        self.bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, self.bishop)  # Coloca al alfil en el centro

#TESTEO MOVIMIENTOS

# Movimiento válido en diagonal

    def test_valid_positions_clear_path(self):
        from_row, from_col = 4, 4
        to_row, to_col = 6, 6  # Movimiento válido en diagonal
        self.assertTrue(self.bishop.valid_positions(from_row, from_col, to_row, to_col))

    def test_invalid_positions_blocked(self):
        from_row, from_col = 4, 4
        blocking_piece = Pawn("WHITE", self.board)
        self.board.set_piece(3, 3, blocking_piece)  # Pone una pieza aliada en el camino
        to_row, to_col = 2, 2  # Movimiento bloqueado
        self.assertFalse(self.bishop.valid_positions(from_row, from_col, to_row, to_col))

    def test_valid_capture_opponent(self):
        from_row, from_col = 4, 4
        opponent_piece = Pawn("BLACK", self.board)
        self.board.set_piece(6, 6, opponent_piece)  # Pone una pieza contraria en el destino
        to_row, to_col = 6, 6  # Movimiento válido para capturar
        self.assertTrue(self.bishop.valid_positions(from_row, from_col, to_row, to_col))

if __name__ == '__main__':
    unittest.main()