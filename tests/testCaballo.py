import unittest
from chess.knight import Knight
from chess.board import Board

class TestKnightSymbol(unittest.TestCase):

    def setUp(self):
        self.board = Board(for_test=True)  # Inicializa el tablero vacío
        self.knight = Knight('WHITE', self.board)

# simbolos piezas caballos (blanco y negro)

    def test_knight_symbol_white(self):
        board = Board()
        knight = Knight("WHITE", board)
        self.assertEqual(knight.symbol(), 'N')

    def test_knight_symbol_black(self):
        board = Board()
        knight = Knight("BLACK", board)
        self.assertEqual(knight.symbol(), 'n')

# testeo movimientos validos

    def test_valid_moves(self):
        """Verifica movimientos válidos en forma de 'L'."""
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
                self.assertTrue(self.knight.is_valid_piece_move(self.board, from_pos, to_pos))

# testeo de movimientos invalidos

    def test_invalid_moves(self):
        """Verifica movimientos inválidos que no cumplen la forma de 'L'."""
        invalid_moves = [
            ((4, 4), (4, 6)),  # Movimiento horizontal (no válido para un caballo)
            ((4, 4), (6, 6)),  # Movimiento diagonal (no válido para un caballo)
            ((4, 4), (5, 5)),  # Movimiento recto (no válido para un caballo)
            ((4, 4), (4, 3)),  # Movimiento horizontal (no válido para un caballo)
        ]
        for from_pos, to_pos in invalid_moves:
            with self.subTest(from_pos=from_pos, to_pos=to_pos):
                self.assertFalse(self.knight.is_valid_piece_move(self.board, from_pos, to_pos))


if __name__ == '__main__':
    unittest.main()
