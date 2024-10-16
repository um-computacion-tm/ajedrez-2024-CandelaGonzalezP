"""
import unittest
from chess.pieces import Piece
from chess.board import Board
from chess.bishop import Bishop
from chess.pawn import Pawn
from chess.rook import Rook
from chess.queen import Queen
from unittest.mock import MagicMock

class TestPieces(unittest.TestCase):
    
    def test_get_color(self):
        piece = Piece("BLACK", None)  # Asume que la pieza necesita un color y el tablero
        self.assertEqual(piece.get_color(), "BLACK")


    def setUp(self):
        self.board = MagicMock()  # Mockeamos el tablero
        self.piece = Piece("WHITE", self.board)  # Creamos una pieza genérica

# Test para movimiento en una dirección vacía

    def test_empty_board_moves(self):
        self.board.get_piece.side_effect = lambda row, col: None
        directions = [(0, 1)]  # Dirección hacia la derecha
        
        valid_moves = self.piece.find_valid_moves(3, 3, directions)

        expected_moves = [(3, 4), (3, 5), (3, 6), (3, 7)]  # Movimientos válidos hacia la derecha
        self.assertEqual(valid_moves, expected_moves)

# Test para movimiento con una captura

    def test_capture_opponent_piece(self):
        mock_opponent_piece = MagicMock()
        mock_opponent_piece.get_color.return_value = "BLACK"
        self.board.get_piece.side_effect = lambda row, col: mock_opponent_piece if (row, col) == (3, 5) else None
        
        directions = [(0, 1)]  # Dirección hacia la derecha
        valid_moves = self.piece.find_valid_moves(3, 3, directions)

        expected_moves = [(3, 4), (3, 5)]
        self.assertEqual(valid_moves, expected_moves)

# Test para movimiento restringido a un solo paso

    def test_single_step_move(self):
        self.board.get_piece.side_effect = lambda row, col: None
        directions = [(0, 1)]  # Dirección hacia la derecha
        
        valid_moves = self.piece.find_valid_moves(3, 3, directions, single_step=True)

        expected_move = [(3, 4)]  # Solo puede moverse un paso a la derecha
        self.assertEqual(valid_moves, expected_move)

# Test para verificar que se detiene cuando encuentra una pieza amiga

    def test_blocked_by_own_piece(self):
        mock_own_piece = MagicMock()
        mock_own_piece.get_color.return_value = "WHITE"
        self.board.get_piece.side_effect = lambda row, col: mock_own_piece if (row, col) == (3, 4) else None

        directions = [(0, 1)]  # Dirección hacia la derecha
        valid_moves = self.piece.find_valid_moves(3, 3, directions)

        expected_moves = []  # No hay movimientos válidos
        self.assertEqual(valid_moves, expected_moves)



if __name__ == '__main__':
    unittest.main()
"""