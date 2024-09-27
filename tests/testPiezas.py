import unittest
from chess.pieces import Piece
from chess.board import Board

class TestPieces(unittest.TestCase):
    
    def test_get_color(self):
        piece = Piece("BLACK", None)  # Asume que la pieza necesita un color y el tablero
        self.assertEqual(piece.get_color(), "BLACK")


    def test_valid_positions(self):
        piece = Piece("BLACK", None)
        piece.get_possible_positions = lambda x, y: [(3, 3)]  # Mockea los posibles movimientos
        self.assertTrue(piece.valid_positions(0, 0, 3, 3))

    def test_possible_diagonal_positions(self):
        piece = Piece("BLACK", None)
        self.assertEqual(piece.possible_diagonal_positions(0, 0), ())


    def test_possible_orthogonal_positions(self):
        piece = Piece("BLACK", None)
        piece.possible_positions_vd = lambda row, col: [(1, 0), (2, 0)]
        piece.possible_positions_va = lambda row, col: [(0, 1), (0, 2)]
        result = piece.possible_orthogonal_positions(0, 0)
        self.assertEqual(result, [(1, 0), (2, 0), (0, 1), (0, 2)])

    def test_possible_positions_vd(self):
        board = Board(for_test=True)
        piece = Piece("BLACK", board) 
        board.set_piece(3, 2, Piece("WHITE", board))  # Coloca una pieza de diferente color en la posición (3, 2)
        possibles = piece.possible_positions_vd(1, 2)
        self.assertEqual(possibles, [(2, 2), (3, 2)])       # Verifica que la función devuelve las posiciones hasta que encuentra una pieza blanca

    def test_possible_positions_va(self):
        board = Board(for_test=True)
        piece = Piece("BLACK", board) 
        possibles = piece.possible_positions_va(4, 2)
        self.assertEqual(possibles, [(3, 2), (2, 2), (1, 2), (0, 2)])        # Verifica que la función devuelve las posiciones hacia arriba desde la fila 4 en la columna 2

if __name__ == '__main__':
    unittest.main()
