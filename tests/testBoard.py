import unittest
from chess.board import Board

class TestBoard(unittest.TestCase):

    def test_str_board(self):                #Inicializa el tablero y compara la salida esperada con la real utilizando simbolos
        board = Board()
        self.assertEqual(
            str(board),
            (
                "♖♘♗♕♔♗♘♖\n"
                "♙♙♙♙♙♙♙♙\n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "♟♟♟♟♟♟♟♟\n"
                "♜♞♝♛♚♝♞♜\n"
            )
        )

    def setUp(self):                                                    #Configura un tablero para cada prueba.
        self.board = Board()

    def test_initial_rook_placement(self):                              #Prueba la colocación inicial de las torres.
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)

    def test_initial_king_placement(self):                              #Prueba la colocación inicial de los reyes.
        black_king = self.board.get_piece(0, 4)
        white_king = self.board.get_piece(7, 4)
        self.assertIsInstance(black_king, King)
        self.assertIsInstance(white_king, King)


    def test_empty_squares(self):                                        #Prueba que las casillas vacías no contienen piezas.
        empty_positions = [
            (2, 0), (3, 3), (4, 4), (5, 5), (3, 2), (4, 1)
        ]
        for position in empty_positions:
            self.assertIsNone(self.board.get_piece(*position))


    def test_rook_positions(self):                                        #Prueba la posición de las torres.
        board = Board()
        board_str = str(board)
        self.assertEqual(board_str[0], "♖")  # Torre en (0,0)
        self.assertEqual(board_str[7], "♖")  # Torre en (0,7)
        self.assertEqual(board_str[-1], "♜")  # Torre en (7,7)
        self.assertEqual(board_str[-8], "♜")  # Torre en (7,0)

    def test_knight_positions(self):                                      #Prueba la posición de los caballos.
        board = Board()
        board_str = str(board)
        self.assertEqual(board_str[1], "♘")  # Caballo en (0,1)
        self.assertEqual(board_str[6], "♘")  # Caballo en (0,6)
        self.assertEqual(board_str[-2], "♞")  # Caballo en (7,6)
        self.assertEqual(board_str[-7], "♞")  # Caballo en (7,1)

    def test_bishop_positions(self):                                     #Prueba la posición de los alfiles.
        board = Board()
        board_str = str(board)
        self.assertEqual(board_str[2], "♗")  # Alfil en (0,2)
        self.assertEqual(board_str[5], "♗")  # Alfil en (0,5)
        self.assertEqual(board_str[-3], "♝")  # Alfil en (7,5)
        self.assertEqual(board_str[-6], "♝")  # Alfil en (7,2)

    def test_queen_positions(self):                                      #Prueba la posición de las reinas.
        board = Board()
        board_str = str(board)
        self.assertEqual(board_str[3], "♕")  # Reina en (0,3)
        self.assertEqual(board_str[-5], "♛")  # Reina en (7,3)

    def test_king_positions(self):                                       #Prueba la posición de los reyes.
        board = Board()
        board_str = str(board)
        self.assertEqual(board_str[4], "♔")  # Rey en (0,4)
        self.assertEqual(board_str[-4], "♚")  # Rey en (7,4)

    def test_pawn_positions(self):                                       #Prueba la posición de los peones.

        board = Board()
        board_str = str(board)
        self.assertEqual(board_str[8:16], "♙♙♙♙♙♙♙♙")  # Peones negros en (1,0) a (1,7)
        self.assertEqual(board_str[-16:-8], "♟♟♟♟♟♟♟♟")  # Peones blancos en (6,0) a (6,7)

if __name__ == '__main__':
    unittest.main()
