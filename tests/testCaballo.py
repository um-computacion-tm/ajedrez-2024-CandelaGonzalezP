"""
import unittest
from chess.knight import Knight
from chess.board import Board

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.board = Board(for_test=True)  # Inicializa el tablero vacío
        self.knight = Knight('WHITE', self.board)

# Simbolos piezas caballos (blanco y negro)

    def test_knight_symbol_white(self):
        board = Board()
        knight = Knight("WHITE", board)
        self.assertEqual(knight.symbol(), '♘')

    def test_knight_symbol_black(self):
        board = Board()
        knight = Knight("BLACK", board)
        self.assertEqual(knight.symbol(), '♞')

# Testeo movimientos válidos

    def test_valid_moves(self):
        valid_moves = [
            ((4, 4), (6, 5)),  # Movimiento en L hacia abajo y derecha
            ((4, 4), (6, 3)),  # Movimiento en L hacia abajo e izquierda
            ((4, 4), (2, 5)),  # Movimiento en L hacia arriba y derecha
            ((4, 4), (2, 3)),  # Movimiento en L hacia arriba e izquierda
            ((4, 4), (5, 6)),  # Movimiento en L hacia la derecha
            ((4, 4), (5, 2)),  # Movimiento en L hacia la izquierda
        ]
        for from_pos, to_pos in valid_moves:
            with self.subTest(from_pos=from_pos, to_pos=to_pos):
                self.assertTrue(self.knight.knight_valid_position(self.board, from_pos, to_pos))

# Testeo de movimientos inválidos

    def test_invalid_moves(self):
        invalid_moves = [
            ((4, 4), (4, 6)),  # Movimiento horizontal (no válido para un caballo)
            ((4, 4), (6, 6)),  # Movimiento diagonal (no válido para un caballo)
            ((4, 4), (5, 5)),  # Movimiento recto (no válido para un caballo)
            ((4, 4), (4, 3)),  # Movimiento horizontal (no válido para un caballo)
        ]
        for from_pos, to_pos in invalid_moves:
            with self.subTest(from_pos=from_pos, to_pos=to_pos):
                self.assertFalse(self.knight.knight_valid_position(self.board, from_pos, to_pos))


if __name__ == '__main__':
    unittest.main()
"""