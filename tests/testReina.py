import unittest
from chess.queen import Queen
from chess.board import Board
from chess.pawn import Pawn
from chess.exceptions import *
from unittest.mock import MagicMock



class TestQueenOrthogonalMoves(unittest.TestCase):

# simbolos piezas reinas (blanco y negro)

    def test_queen_symbol_white(self):
        board = Board()
        queen = Queen("WHITE", board)
        self.assertEqual(queen.symbol(), 'Q')

    def test_queen_symbol_black(self):
        board = Board()
        queen = Queen("BLACK", board)
        self.assertEqual(queen.symbol(), 'q')

#movimientos validos

    def setUp(self):
        self.board = MagicMock()
        self.white_queen = Queen("White", self.board)

    def test_valid_moves(self):
        self.board.get_piece.side_effect = lambda row, col: None

        # Verifica movimientos válidos (diagonal, vertical y horizontal)
        valid_moves = self.white_queen.calculate_possible_moves(3, 3)
        expected_moves = [
            (4, 3), (2, 3),  # Abajo y Arriba
            (3, 4), (3, 2),  # Derecha e Izquierda
            (4, 4), (4, 2),  # Diagonal Abajo Derecha e Izquierda
            (2, 4), (2, 2),  # Diagonal Arriba Derecha e Izquierda
        ]
        self.assertTrue(all(move in valid_moves for move in expected_moves))

    def test_capture_piece(self):
        mock_black_piece = MagicMock()
        mock_black_piece.get_color.return_value = "Black"
        self.board.get_piece.side_effect = lambda row, col: mock_black_piece if (row, col) == (5, 5) else None
        valid_moves = self.white_queen.calculate_possible_moves(4, 4)
        self.assertIn((5, 5), valid_moves)  # La reina debe poder capturar en (5, 5)

    def test_invalid_move(self):
        mock_white_piece = MagicMock()
        mock_white_piece.get_color.return_value = "White"
        self.board.get_piece.side_effect = lambda row, col: mock_white_piece if (row, col) == (5, 5) else None
        valid_moves = self.white_queen.calculate_possible_moves(4, 4)
        self.assertNotIn((5, 5), valid_moves)  # La reina no debe poder moverse a (5, 5)


    def test_restrict_to_single_step(self):
        board = MagicMock()
        queen = Queen("White", board)
        board.get_piece.side_effect = lambda row, col: None

        valid_moves = queen._calculate_moves_in_directions(4, 4, [(1, 0)], restrict_to_single_step=True)
        self.assertEqual(valid_moves, [(5, 4)]) 
















if __name__ == "__main__":
    unittest.main()