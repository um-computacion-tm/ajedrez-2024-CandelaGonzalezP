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

# Verifica que el tablero esté vacío cuando se inicializa en modo de prueba.

    def test_init(self):
        board = Board(for_test=True)
        self.assertIsNone(board.get_piece(0, 0))  # La posición [0,0] está vacía

# Verifica la conversión del tablero a una cadena, asegurando que las piezas se representen correctamente.

    def test_str(self):
        board = Board(for_test=True)
        board.set_piece(0, 0, Rook("WHITE", board))
        board_str = str(board)
        self.assertIn("R", board_str)  # Debería haber una 'R' en la representación

# Comprueba que se puede obtener una pieza en una posición válida y que lanza una excepción al acceder a una posición fuera del tablero.

    def test_get_piece(self):
        board = Board()
        piece = board.get_piece(0, 0)
        self.assertIsInstance(piece, Rook)  # Verificar que hay una torre en [0,0]
        with self.assertRaises(OutOfBoard):
            board.get_piece(8, 8)  # Verificar que lanza excepción por fuera del tablero

# Verifica que se pueda colocar una pieza en una posición del tablero.

    def test_set_piece(self):
        board = Board()
        rook = Rook("WHITE", board)
        board.set_piece(0, 0, rook)
        self.assertEqual(board.get_piece(0, 0), rook)

# Comprueba que una pieza se mueva correctamente de una posición a otra en el tablero.

    def test_move(self):
        board = Board()
        board.move(0, 0, 1, 0)  # Mover la torre de [0,0] a [1,0]
        self.assertIsInstance(board.get_piece(1, 0), Rook)
        self.assertIsNone(board.get_piece(0, 0))

# Verifica que se cuenten correctamente las piezas de un color en el tablero.

    def test_count_pieces(self):
        board = Board()
        count_white = board.count_pieces("WHITE")
        count_black = board.count_pieces("BLACK")
        self.assertEqual(count_white, 8)  # 8 piezas blancas al inicio
        self.assertEqual(count_black, 8)  # 8 piezas negras al inicio


if __name__ == '__main__':
    unittest.main()