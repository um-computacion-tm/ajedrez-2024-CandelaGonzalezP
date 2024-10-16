""""import unittest
from chess.bishop import Bishop
from chess.board import Board

class TestBishop(unittest.TestCase):

# Simbolos piezas alfiles (blanco y negro)

    def test_bishop_symbol_white(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        self.assertEqual(bishop.symbol(), '♗')

    def test_bishop_symbol_black(self):
        board = Board()
        bishop = Bishop("BLACK", board)
        self.assertEqual(bishop.symbol(), '♝')

# Inicia tablero
    def setUp(self):
        self.board = Board(for_test=True)
        self.bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, self.bishop)  # Coloca al alfil en el centro

#TESTEO MOVIMIENTOS

# Movimiento válido en diagonal

    # Diagonal hacia arriba a la derecha
    def test_valid_move_up_right(self):
        result = self.bishop.bishop_valid_position(4, 4, 6, 6)
        self.assertTrue(result)

    # Diagonal hacia arriba a la izquierda
    def test_valid_move_up_left(self):
        result = self.bishop.bishop_valid_position(4, 4, 6, 2)
        self.assertTrue(result)

    # Diagonal hacia abajo a la derecha
    def test_valid_move_down_right(self):
        result = self.bishop.bishop_valid_position(4, 4, 2, 6)
        self.assertTrue(result)

    # Diagonal hacia abajo a la izquierda
    def test_valid_move_down_left(self):
        result = self.bishop.bishop_valid_position(4, 4, 2, 2)
        self.assertTrue(result)

# Movimiento inválido que no es diagonal

    def test_invalid_move_up_right(self):
        result = self.bishop.bishop_valid_position(4, 4, 5, 3)
        self.assertTrue(result)

    def test_invalid_move_up_left(self):
        result = self.bishop.bishop_valid_position(4, 4, 5, 5)
        self.assertTrue(result)

    def test_invalid_move_down_right(self):
        result = self.bishop.bishop_valid_position(4, 4, 3, 5)
        self.assertTrue(result)

    def test_invalid_move_down_left(self):
        result = self.bishop.bishop_valid_position(4, 4, 3, 3)
        self.assertTrue(result)

# Movimiento bloqueado por otra pieza

    def test_blocked_by_piece(self):
        self.board.set_piece(5, 5, Bishop("WHITE", self.board))  # Alfil propio bloqueando
        result = self.bishop.bishop_valid_position(4, 4, 6, 6)  # Bloqueado por el alfil en (5, 5)
        self.assertFalse(result)

# Movimiento válido donde termina en una posición con una pieza enemiga

    def test_valid_move_with_enemy_piece(self):
        self.board.set_piece(6, 6, Bishop("BLACK", self.board))  # Alfil enemigo en la posición destino
        result = self.bishop.bishop_valid_position(4, 4, 6, 6)  # Debería ser válido
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
"""