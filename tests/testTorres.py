import unittest
from chess.rook import Rook
from chess.board import Board
from chess.pawn import Pawn

class TestRook(unittest.TestCase):


# simbolos piezas reyes (blanco y negro)

    def test_rook_symbol_white(self):
        board = Board()
        rook = Rook("WHITE", board)
        self.assertEqual(rook.symbol(), 'R')

    def test_rook_symbol_black(self):
        board = Board()
        rook = Rook("BLACK", board)
        self.assertEqual(rook.symbol(), 'r')

# inicializa tablero

    def setUp(self):
        self.board = Board()
        self.rook = Rook("WHITE", self.board)
        self.board.set_piece(4, 4, self.rook)  # Colocamos la torre en (4, 4)

# MOVIMIENTOS

# Testea un movimiento válido hacia arriba
    def test_valid_move_up(self):
        is_possible = self.rook.is_valid_piece_move(4, 4, 3, 4)
        self.assertFalse(is_possible)

# Testea un movimiento válido hacia abajo
    def test_valid_move_down(self):
        is_possible = self.rook.is_valid_piece_move(4, 4, 5, 4)
        self.assertTrue(is_possible)

# Testea un movimiento válido hacia la izquierda
    def test_valid_move_left(self):
        is_possible = self.rook.is_valid_piece_move(4, 4, 4, 3)
        self.assertFalse(is_possible)

# Testea un movimiento válido hacia la derecha
    def test_valid_move_right(self):
        is_possible = self.rook.is_valid_piece_move(4, 4, 4, 5)
        self.assertFalse(is_possible)

# Testea un movimiento inválido en diagonal
    def test_invalid_move_diagonal(self):
        is_possible = self.rook.is_valid_piece_move(4, 4, 3, 3)
        self.assertFalse(is_possible)

# Testea un movimiento inválido que no sea ortogonal
    def test_invalid_move_two_steps(self):
        is_possible = self.rook.is_valid_piece_move(4, 4, 2, 4)
        self.assertFalse(is_possible)

#########################

# MOVIMIENTOS VERTICALES

# descendentes
    def test_move_vertical_desc(self):          
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

# ascendentes
    def test_move_vertical_asc(self):          
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_va(4, 1)
        self.assertEqual(
            possibles,
            [(3, 1), (2, 1), (1, 1), (0, 1)]
        )

# descendentes con pieza propia bloqueando
    def test_move_vertical_desc_with_own_piece(self):        
        board = Board()
        board.set_piece(6, 1, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

# descendentes con pieza enemiga bloqueando
    def test_move_vertical_desc_with_not_own_piece(self):   
        board = Board()
        board.set_piece(6, 1, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )

# MOVIMIENTOS HORIZONTALES

# hacia la derecha
    def test_move_horizontal_right(self):  
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_hr(4, 1)
        self.assertEqual(
            possibles,
            [(4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)]
        )

# hacia la izquierda
    def test_move_horizontal_left(self):  
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_hl(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3), (4, 2), (4, 1), (4, 0)]
        )

# hacia la derecha con pieza propia bloqueando
    def test_move_horizontal_right_with_own_piece(self):  
        board = Board()
        board.set_piece(4, 6, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 4, rook)
        possibles = rook.possible_positions_hr(4, 4)
        self.assertEqual(
            possibles,
            [(4, 5)]
        )

# hacia la derecha con pieza enemiga bloqueando
    def test_move_horizontal_right_with_not_own_piece(self):  
        board = Board()
        board.set_piece(4, 6, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 4, rook)
        possibles = rook.possible_positions_hr(4, 4)
        self.assertEqual(
            possibles,
            [(4, 5), (4, 6)]
        )


if __name__ == '__main__':
    unittest.main()