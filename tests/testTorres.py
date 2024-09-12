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


if __name__ == '__main__':
    unittest.main()
