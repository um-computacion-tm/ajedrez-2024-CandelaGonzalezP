"""
import unittest
from chess.pawn import Pawn
from chess.board import Board

class TestPawn(unittest.TestCase):

# simbolos piezas alfiles (blanco y negro)

    def test_pawn_symbol_white(self):
        board = Board()
        pawn = Pawn("WHITE", board)
        self.assertEqual(pawn.symbol(), 'P')

    def test_pawn_symbol_black(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        self.assertEqual(pawn.symbol(), 'p')

# inicializar tablero

    def setUp(self):
        self.board = Board(for_test=True)
        self.pawn = Pawn("WHITE", self.board)
        self.board.set_piece(6, 4, self.pawn)  # Coloca el peón en su posición inicial (6, 4)

# TESTEOS MOVIMIENTOS

# Movimiento válido hacia adelante (una casilla)
    def test_valid_move_forward(self):
        result = self.pawn.is_valid_piece_move(6, 4, 5, 4)  
        self.assertTrue(result)

# Movimiento válido hacia adelante (dos casillas desde la posición inicial)
    def test_valid_move_forward_two_steps(self):
        result = self.pawn.is_valid_piece_move(6, 4, 4, 4)  
        self.assertTrue(result)

# Movimiento inválido hacia adelante (cuando hay una pieza en el camino)
    def test_invalid_move_blocked(self):
        self.board.set_piece(5, 4, Pawn("WHITE", self.board))  # Coloca una pieza propia en (5, 4)
        result = self.pawn.is_valid_piece_move(6, 4, 5, 4)  
        self.assertFalse(result)

# Movimiento válido de captura en diagonal
    def test_valid_capture_move(self):
        self.board.set_piece(5, 5, Pawn("BLACK", self.board))  # Coloca un peón enemigo en (5, 5)
        result = self.pawn.is_valid_piece_move(6, 4, 5, 5)  
        self.assertTrue(result)

# Movimiento inválido de captura en diagonal (sin pieza enemiga)
    def test_invalid_capture_move_no_piece(self):
        result = self.pawn.is_valid_piece_move(6, 4, 5, 5)  
        self.assertFalse(result)

# Movimiento inválido hacia adelante (más de dos casillas)
    def test_invalid_move_forward_more_than_two_steps(self):
        result = self.pawn.is_valid_piece_move(6, 4, 3, 4)  
        self.assertFalse(result)

# Movimiento inválido hacia atrás
    def test_invalid_move_backward(self):
        result = self.pawn.is_valid_piece_move(6, 4, 7, 4)  
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
"""