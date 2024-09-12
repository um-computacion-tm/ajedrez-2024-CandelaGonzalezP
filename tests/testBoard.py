import unittest
from chess.board import Board
from chess.rook import Rook
from chess.knight import Knight
from chess.bishop import Bishop
from chess.queen import Queen
from chess.king import King
from chess.pawn import Pawn
from chess.exceptions import OutOfBoard

class TestBoard(unittest.TestCase):

    def setUp(self):                                                    #Configura un tablero para cada prueba.
        self.board = Board()


    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "♜♞♝♛♚♝♞♜\n"    
                "♟♟♟♟♟♟♟♟\n"         
                "        \n" 
                "        \n"            
                "        \n"
                "        \n"
                "♙♙♙♙♙♙♙♙\n"
                "♖♘♗♕♔♗♘♖\n" 
            )
        )

    def test_get_piece_out_of_range(self):
        board = Board(for_test=True)

        with self.assertRaises(OutOfBoard) as exc:
            board.get_piece(10, 10)

        self.assertEqual(
            exc.exception.message,
            "La posicion indicada se encuentra fuera del tablero"
        )


if __name__ == '__main__':
    unittest.main()