import unittest 
from chess.king import King
from chess.board import Board

class TestKing(unittest.TestCase):

# simbolos piezas reyes (blanco y negro)

    def test_king_symbol_white(self):
        board = Board()
        king = King("WHITE", board)
        self.assertEqual(king.symbol(), 'K')

    def test_king_symbol_black(self):
        board = Board()
        king = King("BLACK", board)
        self.assertEqual(king.symbol(), 'k')

# Movimientos válidos

    def test_move_up(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (3, 4)  # Una casilla hacia arriba
        self.assertTrue(king.is_valid_piece_move(board, from_pos, to_pos))

    def test_move_down(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (5, 4)  # Una casilla hacia abajo
        self.assertTrue(king.is_valid_piece_move(board, from_pos, to_pos))

    def test_move_right(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (4, 5)  # Una casilla hacia la derecha
        self.assertTrue(king.is_valid_piece_move(board, from_pos, to_pos))

    def test_move_left(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (4, 3)  # Una casilla hacia la izquierda
        self.assertTrue(king.is_valid_piece_move(board, from_pos, to_pos))

    def test_move_up_right(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (3, 5)  # Diagonal hacia arriba a la derecha
        self.assertTrue(king.is_valid_piece_move(board, from_pos, to_pos))

    def test_move_down_left(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (5, 3)  # Diagonal hacia abajo a la izquierda
        self.assertTrue(king.is_valid_piece_move(board, from_pos, to_pos))

# Movimientos inválidos

    def test_invalid_move_up(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (2, 4)  # Dos casillas hacia arriba
        self.assertFalse(king.is_valid_piece_move(board, from_pos, to_pos))

    def test_invalid_diagonal_move(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (2, 2)  # Dos casillas en diagonal
        self.assertFalse(king.is_valid_piece_move(board, from_pos, to_pos))

    def test_invalid_horizontal_jump(self):
        board = Board()
        king = King("WHITE", board)
        from_pos = (4, 4)
        to_pos = (4, 6)  # Dos casillas hacia la derecha
        self.assertFalse(king.is_valid_piece_move(board, from_pos, to_pos))


if __name__ == '__main__':
    unittest.main()