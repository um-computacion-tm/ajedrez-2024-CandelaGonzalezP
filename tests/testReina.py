import unittest
from chess.queen import Queen
from chess.board import Board
from chess.pawn import Pawn

class TestQueenOrthogonalMoves(unittest.TestCase):

    def setUp(self):
        self.board = Board(for_test=True)
        self.queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, self.queen)  # Colocamos la reina en (4, 4)

# Testeo movimientos ORTOGONALES

    def test_valid_positions(self):
        self.assertTrue(self.queen.valid_positions(4, 4, 7, 4))  # hacia (7, 4)
        self.assertTrue(self.queen.valid_positions(4, 4, 0, 4))  # hacia (0, 4)
        self.assertTrue(self.queen.valid_positions(4, 4, 4, 7))  # hacia (4, 7)
        self.assertTrue(self.queen.valid_positions(4, 4, 4, 0))  # hacia (4, 0)

# Movimientos inválidos (fuera de las posiciones ortogonales)

    def test_invalid_positions(self):
        self.assertFalse(self.queen.valid_positions(4, 4, 5, 5))  # diagonal no está en ortogonales
        self.assertFalse(self.queen.valid_positions(4, 4, 2, 2))  # diagonal no está en ortogonales


# Test de movimientos verticales

    def test_move_vertical_desc(self):  # Movimientos verticales descendentes
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 1, queen)
        possibles = queen.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1), (7, 1)]
        )

    def test_move_vertical_asc(self):  # Movimientos verticales ascendentes
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 1, queen)
        possibles = queen.possible_positions_va(4, 1)
        self.assertEqual(
            possibles,
            [(3, 1), (2, 1), (1, 1), (0, 1)]
        )

# Test de movimientos horizontales

    def test_move_horizontal_right(self):  # Movimientos horizontales hacia la derecha
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 1, queen)
        possibles = queen.possible_positions_hr(4, 1)
        self.assertEqual(
            possibles,
            [(4, 2), (4, 3)]
        )

    def test_move_horizontal_left(self):  # Movimientos horizontales hacia la izquierda
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        possibles = queen.possible_positions_hl(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3), (4, 2), (4, 1), (4, 0)]
        )

# Test de limitaciones por piezas propias o enemigas en movimiento vertical

    def test_move_vertical_desc_with_own_piece(self):  # Limita movimiento vertical por pieza propia
        self.board.set_piece(6, 1, Pawn("WHITE", self.board))
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 1, queen)
        possibles = queen.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_desc_with_not_own_piece(self):  # Limita movimiento vertical por pieza enemiga
        self.board.set_piece(6, 1, Pawn("BLACK", self.board))
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 1, queen)
        possibles = queen.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )

# Test de limitaciones por piezas propias o enemigas en movimiento horizontal

    def test_move_horizontal_right_with_own_piece(self):  # Limita movimiento horizontal por pieza propia
        self.board.set_piece(4, 6, Pawn("WHITE", self.board))
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        possibles = queen.possible_positions_hr(4, 4)
        self.assertEqual(
            possibles,
            [(4, 5)]
        )

    def test_move_horizontal_right_with_not_own_piece(self):  # Limita movimiento horizontal por pieza enemiga
        self.board.set_piece(4, 6, Pawn("BLACK", self.board))
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        possibles = queen.possible_positions_hr(4, 4)
        self.assertEqual(
            possibles,
            [(4, 5), (4, 6)]
        )

# Test de movimientos inválidos generales

    def test_invalid_move(self):  
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        is_possible = queen.valid_positions(
            from_row=4,
            from_col=4,
            to_row=1,
            to_col=2,  
        )
        self.assertFalse(is_possible)



if __name__ == "__main__":
    unittest.main()




""" # Test de movimientos diagonales
    def test_move_diagonal(self):  # Movimientos diagonales válidos
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        possibles = queen.possible_diagonal_positions(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5), (6, 6), (7, 7), (3, 3), (2, 2), (1, 1), (0, 0), 
             (5, 3), (6, 2), (7, 1), (3, 5), (2, 6), (1, 7)]
        )


    def test_move_diagonal_with_own_piece(self):  # Limita movimiento diagonal por pieza propia
        self.board.set_piece(6, 6, Pawn("WHITE", self.board))
        queen = Queen("WHITE", self.board)
        self.board.set_piece(4, 4, queen)
        possibles = queen.possible_diagonal_positions(4, 4)
        self.assertEqual(
            possibles,
            [(5, 5)]
        )

        def test_move_diagonal_with_not_own_piece(self):  # Limita movimiento diagonal por pieza enemiga
            self.board.set_piece(6, 6, Pawn("BLACK", self.board))
            queen = Queen("WHITE", self.board)
            self.board.set_piece(4, 4, queen)
            possibles = queen.possible_diagonal_positions(4, 4)
            self.assertEqual(
                possibles,
                [(5, 5), (6, 6)]
            )"""






#falta test movimientos diagonales


