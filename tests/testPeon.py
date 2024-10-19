import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from chess.pawn import Pawn
from chess.board import Board

class TestPawn(unittest.TestCase):

# Simbolos piezas peones (blanco y negro)

    def test_pawn_symbol_white(self):
        board = Board()
        pawn = Pawn("WHITE", board)
        self.assertEqual(pawn.symbol(), '♙')

    def test_pawn_symbol_black(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        self.assertEqual(pawn.symbol(), '♟')

# Inicializar tablero

    def setUp(self):
        self.board = Board(for_test=True)
        self.pawn = Pawn("WHITE", self.board)
        self.board.set_piece(6, 4, self.pawn)  # Coloca el peón en su posición inicial (6, 4)

# TESTEO MOVIMIENTOS

   # Test de movimientos válidos hacia adelante
    def test_valid_move_forward(self):
        result = self.pawn.valid_positions(6, 4, 5, 4)
        self.assertTrue(result)

    def test_valid_move_forward_two_steps(self):
        result = self.pawn.valid_positions(6, 4, 4, 4)
        self.assertTrue(result)

    # Test de movimiento inválido cuando está bloqueado por otra pieza
    def test_invalid_move_blocked(self):
        self.board.set_piece(5, 4, Pawn("WHITE", self.board))  # Coloca un peón blanco en (5, 4) bloqueando
        result = self.pawn.valid_positions(6, 4, 5, 4)
        self.assertFalse(result)

    # Test de movimiento válido de captura en diagonal
    def test_valid_capture_move(self):
        self.board.set_piece(5, 5, Pawn("BLACK", self.board))  # Coloca un peón negro en (5, 5)
        result = self.pawn.valid_positions(6, 4, 5, 5)
        self.assertTrue(result)

    # Test de captura inválida fuera del tablero
    def test_invalid_capture_out_of_bounds(self):
        out_of_bounds_positions = [(-1, 0), (8, 0), (0, -1), (0, 8)]
        for row, col in out_of_bounds_positions:
            result = self.pawn.is_in_bounds(row, col)
            self.assertFalse(result)

    # Test de intento de captura sin pieza para capturar
    def test_invalid_capture_move_no_piece(self):
        result = self.pawn.valid_positions(6, 4, 5, 5)
        self.assertFalse(result)

    # Test de movimiento inválido hacia adelante más de dos casillas
    def test_invalid_move_forward_more_than_two_steps(self):
        result = self.pawn.valid_positions(6, 4, 3, 4)
        self.assertFalse(result)

    # Test de movimiento inválido hacia atrás
    def test_invalid_move_backward(self):
        result = self.pawn.valid_positions(6, 4, 7, 4)
        self.assertFalse(result)






if __name__ == '__main__':
    unittest.main()