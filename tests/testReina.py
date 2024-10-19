import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from chess.queen import Queen
from chess.board import Board
from unittest.mock import MagicMock

class TestQueenValidPositions(unittest.TestCase):

    # Simbolos piezas reinas (blanco y negro)

    def test_queen_symbol_white(self):
        board = Board()
        queen = Queen("WHITE", board)
        self.assertEqual(queen.symbol(), '♕')

    def test_queen_symbol_black(self):
        board = Board()
        queen = Queen("BLACK", board)
        self.assertEqual(queen.symbol(), '♛')

# TESTEO MOVIMIENTOS

    def setUp(self):
        self.board = Board()  # Usamos un tablero real en lugar de simularlo
        self.white_queen = Queen("WHITE", self.board)  # Instancia de la reina blanca

    # Testea un movimiento válido en dirección vertical
    def test_valid_move_vertical(self):
        self.board.set_piece(3, 3, self.white_queen)  # Colocamos la reina en la posición inicial
        move = (3, 3, 5, 3)  # Movimiento vertical hacia abajo
        self.assertTrue(self.white_queen.valid_positions(self.board, move[:2], move[2:]))

    # Testea un movimiento válido en dirección horizontal
    def test_valid_move_horizontal(self):
        self.board.set_piece(3, 3, self.white_queen)  # Colocamos la reina en la posición inicial
        move = (3, 3, 3, 5)  # Movimiento horizontal hacia la derecha
        self.assertTrue(self.white_queen.valid_positions(self.board, move[:2], move[2:]))

    # Testea un movimiento válido en dirección diagonal
    def test_valid_move_diagonal(self):
        self.board.set_piece(3, 3, self.white_queen)  # Colocamos la reina en la posición inicial
        move = (3, 3, 5, 5)  # Movimiento diagonal hacia abajo a la derecha
        self.assertTrue(self.white_queen.valid_positions(self.board, move[:2], move[2:]))

    # Testea un movimiento inválido que no es ni ortogonal ni diagonal
    def test_invalid_move(self):
        self.board.set_piece(3, 3, self.white_queen)  # Colocamos la reina en la posición inicial
        move = (3, 3, 5, 4)  # Movimiento inválido
        self.assertFalse(self.white_queen.valid_positions(self.board, move[:2], move[2:]))

    # Testea un movimiento inválido que intenta moverse a una posición ocupada por una pieza del mismo color
    def test_move_to_same_color_piece(self):
        self.board.set_piece(3, 3, self.white_queen)  # Colocamos la reina en la posición inicial
        self.board.set_piece(5, 5, Queen("WHITE", self.board))  # Colocamos otra reina blanca en la posición destino
        move = (3, 3, 5, 5)  # Movimiento a una posición ocupada por el mismo color
        self.assertFalse(self.white_queen.valid_positions(self.board, move[:2], move[2:]))

    # Testea un movimiento válido que intenta moverse a una posición vacía
    def test_move_to_empty_position(self):
        self.board.set_piece(3, 3, self.white_queen)  # Colocamos la reina en la posición inicial
        move = (3, 3, 5, 5)  # Movimiento a una posición vacía
        self.assertTrue(self.white_queen.valid_positions(self.board, move[:2], move[2:]))


    def test_move_out_of_bounds_above(self):
        # Movimiento fuera de los límites (fuera del tablero por arriba)
        from_pos = (0, 0)  # Posición inicial (superior izquierda)
        to_pos = (-1, 0)   # Intento de mover fuera del tablero
        self.assertFalse(self.white_queen.valid_positions(self.board, from_pos, to_pos))

    def test_move_out_of_bounds_below(self):
        # Movimiento fuera de los límites (fuera del tablero por abajo)
        from_pos = (7, 0)  # Posición inicial (inferior izquierda)
        to_pos = (8, 0)    # Intento de mover fuera del tablero
        self.assertFalse(self.white_queen.valid_positions(self.board, from_pos, to_pos))

    def test_move_out_of_bounds_left(self):
        # Movimiento fuera de los límites (fuera del tablero por la izquierda)
        from_pos = (0, 0)  # Posición inicial (superior izquierda)
        to_pos = (0, -1)   # Intento de mover fuera del tablero
        self.assertFalse(self.white_queen.valid_positions(self.board, from_pos, to_pos))

    def test_move_out_of_bounds_right(self):
        # Movimiento fuera de los límites (fuera del tablero por la derecha)
        from_pos = (0, 7)  # Posición inicial (superior derecha)
        to_pos = (0, 8)    # Intento de mover fuera del tablero
        self.assertFalse(self.white_queen.valid_positions(self.board, from_pos, to_pos))


if __name__ == "__main__":
    unittest.main()

