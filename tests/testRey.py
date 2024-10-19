import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from chess.king import King
from chess.board import Board

class TestKing(unittest.TestCase):

    def test_king_symbol_white(self):
        board = Board()
        king = King("WHITE", board)
        self.assertEqual(king.symbol(), '♔')

    def test_king_symbol_black(self):
        board = Board()
        king = King("BLACK", board)
        self.assertEqual(king.symbol(), '♚')

# TESTEO MOVIMIENTOS

    # Testeo de movimientos válidos
    def test_move_up(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (3, 4)  # Una casilla hacia arriba
        self.assertTrue(king.valid_positions(board, from_pos, to_pos))

    def test_move_down(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (5, 4)  # Una casilla hacia abajo
        self.assertTrue(king.valid_positions(board, from_pos, to_pos))

    def test_move_right(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (4, 5)  # Una casilla hacia la derecha
        self.assertTrue(king.valid_positions(board, from_pos, to_pos))

    def test_move_left(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (4, 3)  # Una casilla hacia la izquierda
        self.assertTrue(king.valid_positions(board, from_pos, to_pos))

    def test_move_up_right(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (3, 5)  # Diagonal hacia arriba a la derecha
        self.assertTrue(king.valid_positions(board, from_pos, to_pos))

    def test_move_down_left(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (5, 3)  # Diagonal hacia abajo a la izquierda
        self.assertTrue(king.valid_positions(board, from_pos, to_pos))

    # Testeo de movimientos inválidos
    def test_invalid_move_up(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (2, 4)  # Dos casillas hacia arriba
        self.assertFalse(king.valid_positions(board, from_pos, to_pos))

    def test_invalid_diagonal_move(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (2, 2)  # Dos casillas en diagonal
        self.assertFalse(king.valid_positions(board, from_pos, to_pos))

    def test_invalid_horizontal_jump(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (4, 6)  # Dos casillas hacia la derecha
        self.assertFalse(king.valid_positions(board, from_pos, to_pos))


    def test_move_out_of_bounds(self):
        board = Board()
        king = King("WHITE", board)

        from_pos = (4, 4)  # Posición actual del rey

        # Movimiento fuera de los límites del tablero (por ejemplo, fila -1 no es válida)
        to_pos = (-1, 4)
        self.assertFalse(king.valid_positions(board, from_pos, to_pos))

        # Movimiento fuera de los límites del tablero (por ejemplo, columna 8 no es válida)
        to_pos = (4, 8)
        self.assertFalse(king.valid_positions(board, from_pos, to_pos))

        # Movimiento dentro de los límites (casilla válida) - se espera True para comparar
        to_pos = (3, 4)  # Una casilla hacia arriba
        self.assertTrue(king.valid_positions(board, from_pos, to_pos))


    def test_move_to_same_color_piece(self):
        board = Board()

        # Colocamos un rey blanco en (4, 4)
        king = King("WHITE", board)
        board.set_piece(4, 4, king)

        # Simulamos que hay una pieza blanca en la posición destino (5, 4)
        board.set_piece(5, 4, King("WHITE", board))  # Otra pieza blanca en la posición destino

        from_pos = (4, 4)  # Posición actual del rey
        to_pos = (5, 4)    # Posición donde está la pieza blanca

        # Verificamos que el movimiento no es válido porque la pieza de destino es del mismo color
        self.assertFalse(king.valid_positions(board, from_pos, to_pos))

    def test_move_to_empty_position(self):
        board = Board()
        
        # Colocamos un rey blanco en (4, 4)
        king = King("WHITE", board)
        board.set_piece(4, 4, king)

        from_pos = (4, 4)  # Posición actual del rey
        to_pos = (5, 4)    # Posición vacía

        # Verificamos que el movimiento es válido porque la posición está vacía
        self.assertTrue(king.valid_positions(board, from_pos, to_pos))



if __name__ == '__main__':
    unittest.main()
