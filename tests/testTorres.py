import unittest
from chess.rook import Rook
from chess.board import Board
from chess.pawn import Pawn

class TestRook(unittest.TestCase):

    def test_str(self):                        #verifica simbolo de pieza (blanca)
        board = Board()
        rook = Rook("WHITE", board)
        self.assertEqual(
            str(rook),
            "♜",
        )


# testeo movimientos verticales ascendentes y descendentes

    def test_move_vertical_desc(self):          #movimientos verticales en descenso de rook          
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_asc(self):          #movimientos verticales en ascenso
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_va(4, 1)
        self.assertEqual(
            possibles,
            [(3, 1), (2, 1), (1, 1), (0, 1)]
        )

    def test_move_vertical_desc_with_own_piece(self):        #limita movimiento de rook de pieza propia
        board = Board()
        board.set_piece(6, 1, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1)]
        )

    def test_move_vertical_desc_with_not_own_piece(self):   #limita movimiento de rook con otra pieza
        board = Board()
        board.set_piece(6, 1, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 1, rook)
        possibles = rook.possible_positions_vd(4, 1)
        self.assertEqual(
            possibles,
            [(5, 1), (6, 1)]
        )

# testo movimientos horizontales derecha e izquierda


    def test_move_horizontal_right(self):  # Movimientos horizontales hacia la derecha
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_hr(4, 1)
        self.assertEqual(
            possibles,
            [(4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7)]
        )

    def test_move_horizontal_left(self):  # Movimientos horizontales hacia la izquierda
        board = Board()
        rook = Rook("WHITE", board)
        possibles = rook.possible_positions_hl(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3), (4, 2), (4, 1), (4, 0)]
        )

    def test_move_horizontal_right_with_own_piece(self):  # Limita movimiento horizontal por pieza propia
        board = Board()
        board.set_piece(4, 6, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 4, rook)
        possibles = rook.possible_positions_hr(4, 4)
        self.assertEqual(
            possibles,
            [(4, 5)]
        )

    def test_move_horizontal_right_with_not_own_piece(self):  # Limita movimiento horizontal por pieza contraria
        board = Board()
        board.set_piece(4, 6, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 4, rook)
        possibles = rook.possible_positions_hr(4, 4)
        self.assertEqual(
            possibles,
            [(4, 5), (4, 6)]
        )

    def test_move_horizontal_left_with_own_piece(self):  # Limita movimiento hacia la izquierda por pieza propia
        board = Board()
        board.set_piece(4, 2, Pawn("WHITE", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 4, rook)
        possibles = rook.possible_positions_hl(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3)]
        )

    def test_move_horizontal_left_with_not_own_piece(self):  # Limita movimiento hacia la izquierda por pieza contraria
        board = Board()
        board.set_piece(4, 2, Pawn("BLACK", board))
        rook = Rook("WHITE", board)
        board.set_piece(4, 4, rook)
        possibles = rook.possible_positions_hl(4, 4)
        self.assertEqual(
            possibles,
            [(4, 3), (4, 2)]
        )

#testo movimientos en diagonal invalido

    def test_move_diagonal_desc(self):                 #movimiento en diagonal invalido
        board = Board()
        rook = board.get_piece(col=0, row=0)
        is_possible = rook.valid_positions(
            from_row=0,
            from_col=0,
            to_row=1,
            to_col=1,
        )
        self.assertFalse(is_possible)


# testeo para mejorar porcentaje de codigo

    def setUp(self):
        self.board = Board()
        self.rook = Rook('white', self.board)
        self.board.set_piece(4, 4, self.rook)  # Colocamos la torre en (4, 4)

    def test_possible_positions_hl_with_friendly_piece(self):
        # Colocamos una pieza amiga en (4, 3)
        friendly_piece = Rook('white', self.board)
        self.board.set_piece(4, 3, friendly_piece)
        
        # Colocamos casillas vacías a la izquierda de la torre
        self.board.set_piece(4, 2, None)
        self.board.set_piece(4, 1, None)
        self.board.set_piece(4, 0, None)
        
        # Las posiciones esperadas deben incluir hasta la pieza amiga
        expected_positions = []
        actual_positions = self.rook.possible_positions_hl(4, 4)
        self.assertEqual(actual_positions, expected_positions)



if __name__ == '__main__':
    unittest.main()
