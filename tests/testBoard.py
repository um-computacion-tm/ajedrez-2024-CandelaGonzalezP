import unittest
from chess.board import Board
from chess.rook import Rook
from chess.knight import Knight
from chess.bishop import Bishop
from chess.queen import Queen
from chess.king import King
from chess.pawn import Pawn
from chess.exceptions import *


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board=Board()
        self.initialize_board()


#  Verifica que la excepcion se largue con posiciones invalidas

    def test_get_piece_valid_position(self):
        # Test para una posición válida (dentro del tablero)
        piece = self.board.get_piece(0, 0)
        self.assertIsNotNone(piece)  # Verifica que se obtenga una pieza (si hay una en esa posición)

    def test_get_piece_invalid_row(self):
        # Test para una fila inválida (fuera del tablero)
        with self.assertRaises(OriginInvalidMove):
            self.board.get_piece(8, 4)  # Fila fuera de los límites

    def test_get_piece_invalid_col(self):
        # Test para una columna inválida (fuera del tablero)
        with self.assertRaises(OriginInvalidMove):
            self.board.get_piece(3, -1)  # Columna fuera de los límites

    def test_get_piece_invalid_both(self):
        # Test para una fila y columna inválidas
        with self.assertRaises(OriginInvalidMove):
            self.board.get_piece(10, 10)  # Ambas fuera de los límites


# verifica que al mover una pieza y luego intentar colocar otra pieza en la misma posición, se actualice correctamente. 

    def test_set_piece_overwrite(self):
        # Establecer una torre blanca en la posición [0,0]
        rook = Rook("WHITE", self.board)
        self.board.set_piece(0, 0, rook)
        self.assertEqual(self.board.get_piece(0, 0), rook)
        # Establecer un alfil negro en la misma posición
        bishop = Bishop("BLACK", self.board)
        self.board.set_piece(0, 0, bishop)
        # Verificar que la torre ha sido reemplazada por el alfil negro
        self.assertEqual(self.board.get_piece(0, 0), bishop)

    def test_set_multiple_pieces(self):
        # Establecer varias piezas
        rook = Rook("WHITE", self.board)
        bishop = Bishop("BLACK", self.board)
        king = King("WHITE", self.board)
        self.board.set_piece(0, 0, rook)
        self.board.set_piece(0, 2, bishop)
        self.board.set_piece(0, 4, king)

        # Verificar que cada pieza está en la posición correcta
        self.assertEqual(self.board.get_piece(0, 0), rook)
        self.assertEqual(self.board.get_piece(0, 2), bishop)
        self.assertEqual(self.board.get_piece(0, 4), king)

# Comprueba que una pieza se mueva correctamente de una posición a otra en el tablero.

    def test_move_rook(self):
        # Mover la torre negra de [0,0] a [1,0]
        self.board.move(0, 0, 1, 0)
        self.assertIsInstance(self.board.get_piece(1, 0), Rook)
        self.assertIsNone(self.board.get_piece(0, 0))

    def test_move_bishop(self):
        # Mover el alfil negro de [0,2] a [1,3]
        self.board.move(0, 2, 1, 3)
        self.assertIsInstance(self.board.get_piece(1, 3), Bishop)
        self.assertIsNone(self.board.get_piece(0, 2))

    def test_move_king(self):
        # Mover el rey negro de [0,4] a [1,4]
        self.board.move(0, 4, 1, 4)
        self.assertIsInstance(self.board.get_piece(1, 4), King)
        self.assertIsNone(self.board.get_piece(0, 4))

    def test_move_queen(self):
        # Mover la reina negra de [0,3] a [1,3]
        self.board.move(0, 3, 1, 3)
        self.assertIsInstance(self.board.get_piece(1, 3), Queen)
        self.assertIsNone(self.board.get_piece(0, 3))

    def test_move_knight(self):
        # Mover el caballo negro de [0,1] a [2,2]
        self.board.move(0, 1, 2, 2)
        self.assertIsInstance(self.board.get_piece(2, 2), Knight)
        self.assertIsNone(self.board.get_piece(0, 1))

    def test_move_pawn(self):
        # Mover un peón negro de [1,0] a [2,0]
        self.board.move(1, 0, 2, 0)
        self.assertIsInstance(self.board.get_piece(2, 0), Pawn)
        self.assertIsNone(self.board.get_piece(1, 0))


# Verifica que se cuenten correctamente las piezas de un color en el tablero.

    def initialize_board(self):
        # Colocar las piezas en sus posiciones iniciales
        self.board.set_piece(0, 0, Rook("BLACK", self.board))
        self.board.set_piece(0, 1, Knight("BLACK", self.board))
        self.board.set_piece(0, 2, Bishop("BLACK", self.board))
        self.board.set_piece(0, 3, Queen("BLACK", self.board))
        self.board.set_piece(0, 4, King("BLACK", self.board))
        self.board.set_piece(0, 5, Bishop("BLACK", self.board))
        self.board.set_piece(0, 6, Knight("BLACK", self.board))
        self.board.set_piece(0, 7, Rook("BLACK", self.board))
        
        for col in range(8):
            self.board.set_piece(1, col, Pawn("BLACK", self.board))
            self.board.set_piece(6, col, Pawn("WHITE", self.board))
        
        self.board.set_piece(7, 0, Rook("WHITE", self.board))
        self.board.set_piece(7, 1, Knight("WHITE", self.board))
        self.board.set_piece(7, 2, Bishop("WHITE", self.board))
        self.board.set_piece(7, 3, Queen("WHITE", self.board))
        self.board.set_piece(7, 4, King("WHITE", self.board))
        self.board.set_piece(7, 5, Bishop("WHITE", self.board))
        self.board.set_piece(7, 6, Knight("WHITE", self.board))
        self.board.set_piece(7, 7, Rook("WHITE", self.board))

    def test_count_pieces(self):
        count_white = self.board.count_pieces("WHITE")
        count_black = self.board.count_pieces("BLACK")
        self.assertEqual(count_white, 16)  # 8 peones + 8 piezas (torres, caballos, alfiles, rey, reina)
        self.assertEqual(count_black, 16)  # 8 peones + 8 piezas (torres, caballos, alfiles, rey, reina)


if __name__ == '__main__':
    unittest.main()