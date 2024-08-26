import unittest
from chess.bishop import Bishop
from chess.board import Board

class TestBishop(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_bishop_moves(self):
        bishop = Bishop((2, 3), "WHITE")
        self.board.place_piece(bishop, (2, 3))
        moves = bishop.get_possible_moves(self.board)

        # Movimientos esperados en un tablero vacío
        expected_moves = [
            (3, 4), (4, 5), (5, 6), (6, 7),  # Diagonal arriba derecha
            (3, 2), (4, 1), (5, 0),          # Diagonal arriba izquierda
            (1, 4), (0, 5),                  # Diagonal abajo derecha
            (1, 2), (0, 1)                   # Diagonal abajo izquierda
        ]
        self.assertEqual(set(moves), set(expected_moves))

if __name__ == '__main__':
    unittest.main()
