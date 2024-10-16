"""
import unittest
from chess.rook import Rook
from chess.board import Board

class TestRook(unittest.TestCase):

# Simbolos piezas reyes (blanco y negro)

    def test_rook_symbol_white(self):
        board = Board()
        rook = Rook("WHITE", board)
        self.assertEqual(rook.symbol(), '♖')

    def test_rook_symbol_black(self):
        board = Board()
        rook = Rook("BLACK", board)
        self.assertEqual(rook.symbol(), '♜') 

# Inicializa el tablero

    def setUp(self):
        self.board = Board()
        self.rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 4, self.rook)  # Colocamos la torre en (4, 4)

# TESTEO MOVIMIENTOS

    # Testea un movimiento válido hacia arriba
    def test_valid_move_up(self):
        is_possible = self.rook.rook_valid_positions(4, 4, 3, 4)
        self.assertTrue(is_possible)

    # Testea un movimiento válido hacia abajo
    def test_valid_move_down(self):
        is_possible = self.rook.rook_valid_positions(4, 4, 5, 4)
        self.assertTrue(is_possible)

    # Testea un movimiento válido hacia la izquierda
    def test_valid_move_left(self):
        is_possible = self.rook.rook_valid_positions(4, 4, 4, 3)
        self.assertTrue(is_possible)

    # Testea un movimiento válido hacia la derecha
    def test_valid_move_right(self):
        is_possible = self.rook.rook_valid_positions(4, 4, 4, 5)
        self.assertTrue(is_possible)

    # Testea un movimiento inválido en diagonal
    def test_invalid_move_diagonal(self):
        is_possible = self.rook.rook_valid_positions(4, 4, 3, 3)
        self.assertFalse(is_possible)

    # Testea un movimiento inválido que no sea ortogonal
    def test_invalid_move_two_steps(self):
        is_possible = self.rook.rook_valid_positions(4, 4, 2, 4)
        self.assertTrue(is_possible)


if __name__ == '__main__':
    unittest.main()
"""