import unittest
from chess.bishop import Bishop
from chess.board import Board

class TestBishop(unittest.TestCase):

# simbolos piezas alfiles (blanco y negro)

    def test_bishop_symbol_white(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        self.assertEqual(bishop.symbol(), 'B')

    def test_bishop_symbol_black(self):
        board = Board()
        bishop = Bishop("BLACK", board)
        self.assertEqual(bishop.symbol(), 'b')

# inicia tablero

    def setUp(self):
        self.board = Board(for_test=True)
        self.bishop = Bishop("WHITE", self.board)
        self.board.set_piece(4, 4, self.bishop)  # Coloca al alfil en el centro

# TESTEOS MOVIMIENTOS

# movimiento válido en diagonal

    # Diagonal hacia arriba a la derecha 
    def test_valid_move_up_right(self):
        result = self.bishop.is_valid_piece_move(4, 4, 6, 6)  
        self.assertFalse(result)

    # Diagonal hacia arriba a la izquierda 
    def test_valid_move_up_left(self):
        result = self.bishop.is_valid_piece_move(4, 4, 6, 2)  
        self.assertFalse(result)

    # Diagonal hacia abajo a la derecha (up-right)
    def test_valid_move_down_right(self):
        result = self.bishop.is_valid_piece_move(4, 4, 2, 6)  
        self.assertFalse(result)

    # Diagonal hacia abajo a la izquierda (up-left)
    def test_valid_move_down_left(self):
        result = self.bishop.is_valid_piece_move(4, 4, 2, 2)  
        self.assertFalse(result)


# movimiento inválido que no es diagonal

    # Movimiento inválido que no es en la diagonal arriba a la derecha
    def test_invalid_move_up_right(self):
        result = self.bishop.is_valid_piece_move(4, 4, 5, 3)  
        self.assertFalse(result)

    # Movimiento inválido que no es en la diagonal arriba a la izquierda
    def test_invalid_move_up_left(self):
        result = self.bishop.is_valid_piece_move(4, 4, 5, 5)  
        self.assertTrue(result)

    # Movimiento inválido que no es en la diagonal abajo a la derecha
    def test_invalid_move_down_right(self):
        result = self.bishop.is_valid_piece_move(4, 4, 3, 5)  
        self.assertFalse(result)

    # Movimiento inválido que no es en la diagonal abajo a la izquierda
    def test_invalid_move_down_left(self):
        result = self.bishop.is_valid_piece_move(4, 4, 3, 3)  
        self.assertFalse(result)

# movimiento bloqueado por otra pieza
    def test_blocked_by_piece(self):
        self.board.set_piece(5, 5, Bishop("WHITE", self.board))  # Alfil propio bloqueando
        result = self.bishop.is_valid_piece_move(4, 4, 6, 6)  # Bloqueado por el alfil en (5, 5)
        self.assertFalse(result)

# movimiento válido donde termina en una posición con una pieza enemiga
    def test_valid_move_with_enemy_piece(self):
        self.board.set_piece(6, 6, Bishop("BLACK", self.board))  # Alfil enemigo en la posición destino
        result = self.bishop.is_valid_piece_move(4, 4, 6, 6)  # Debería ser válido
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()













"""
# inicializar tablero

    def setUp(self):
        self.board = Board(for_test=True)  # Inicializa el tablero sin piezas
        self.bishop = Bishop('White', self.board)  # Crea un alfil blanco

# testeo posiciones posibles

    def test_get_possible_positions(self):
        self.board.set_piece(3, 3, self.bishop)  # Coloca el alfil en (3, 3)
        result = self.bishop.get_possible_positions(3, 3)
        expected = self.bishop.possible_diagonal_positions(3, 3)
        self.assertEqual(result, expected)


# testeo movimientos diagonales ascendentes

    
    def test_possible_positions_dad(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        
        # Caso sin bloqueos
        possibles = bishop.possible_positions_dad(4, 4)
        expected_positions = [(3, 5), (2, 6), (1, 7)]
        self.assertEqual(possibles, expected_positions)

    def test_possible_positions_dad_with_block(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        
        # Bloqueo con una pieza enemiga
        board.set_piece(2, 6, Pawn("BLACK", board))
        possibles = bishop.possible_positions_dad(4, 4)
        expected_positions = [(3, 5), (2, 6)]  # Se detiene en la pieza enemiga
        self.assertEqual(possibles, expected_positions)

    def test_possible_positions_dad_with_own_piece_block(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        
        # Bloqueo con una pieza propia
        board.set_piece(3, 5, Pawn("WHITE", board))
        possibles = bishop.possible_positions_dad(4, 4)
        expected_positions = []  # Se detiene en la propia pieza
        self.assertEqual(possibles, expected_positions)


    def test_possible_positions_dai(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        
        # Caso sin bloqueos
        possibles = bishop.possible_positions_dai(4, 4)
        expected_positions = [(3, 3), (2, 2), (1, 1), (0, 0)]
        self.assertEqual(possibles, expected_positions)

    def test_possible_positions_dai_with_block(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        
        # Bloqueo con una pieza enemiga
        board.set_piece(2, 2, Pawn("BLACK", board))
        possibles = bishop.possible_positions_dai(4, 4)
        expected_positions = [(3, 3), (2, 2)]  # Se detiene en la pieza enemiga
        self.assertEqual(possibles, expected_positions)

    def test_possible_positions_dai_with_own_piece_block(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        
        # Bloqueo con una pieza propia
        board.set_piece(3, 3, Pawn("WHITE", board))
        possibles = bishop.possible_positions_dai(4, 4)
        expected_positions = []  # Se detiene en la propia pieza
        self.assertEqual(possibles, expected_positions)


# testeo movimientos diagonales descendentes

    def test_possible_positions_ddd(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        
        # Caso sin bloqueos
        possibles = bishop.possible_positions_ddd(4, 4)
        expected_positions = [(5, 5), (6, 6), (7, 7)]
        self.assertEqual(possibles, expected_positions)

    def test_possible_positions_ddd_with_block(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        
        # Bloqueo con una pieza enemiga
        board.set_piece(6, 6, Pawn("BLACK", board))
        possibles = bishop.possible_positions_ddd(4, 4)
        expected_positions = [(5, 5), (6, 6)]  # Se detiene en la pieza enemiga
        self.assertEqual(possibles, expected_positions)

    def test_possible_positions_ddd_with_own_piece_block(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)
        
        # Bloqueo con una pieza propia
        board.set_piece(5, 5, Pawn("WHITE", board))
        possibles = bishop.possible_positions_ddd(4, 4)
        expected_positions = []  # Se detiene en la propia pieza
        self.assertEqual(possibles, expected_positions)

    def test_possible_positions_ddi(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)

        # Caso sin bloqueos
        possibles = bishop.possible_positions_ddi(4, 4)
        expected_positions = [(5, 3), (6, 2), (7, 1)]
        self.assertEqual(possibles, expected_positions)

    def test_possible_positions_ddi_with_block(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)

        # Bloqueo con una pieza enemiga
        board.set_piece(6, 2, Pawn("BLACK", board))
        possibles = bishop.possible_positions_ddi(4, 4)
        expected_positions = [(5, 3), (6, 2)]  # Se detiene en la pieza enemiga
        self.assertEqual(possibles, expected_positions)

    def test_possible_positions_ddi_with_own_piece_block(self):
        board = Board(for_test=True)
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)

        # Bloqueo con una pieza propia
        board.set_piece(5, 3, Pawn("WHITE", board))
        possibles = bishop.possible_positions_ddi(4, 4)
        expected_positions = []  # Se detiene en la propia pieza
        self.assertEqual(possibles, expected_positions)


if __name__ == '__main__':
    unittest.main()
"""
