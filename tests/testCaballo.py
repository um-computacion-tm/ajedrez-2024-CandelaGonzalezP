import unittest
from chess.knight import Knight
from chess.board import Board

class TestKnightSymbol(unittest.TestCase):

    def setUp(self):
        self.board = Board(for_test=True)  # Inicializa el tablero vacío
        self.knight = Knight('WHITE', self.board)

# simbolos piezas caballos (blanco y negro)

    def test_knight_symbol_white(self):
        board = Board()
        knight = Knight("WHITE", board)
        self.assertEqual(knight.symbol(), 'N')

    def test_knight_symbol_black(self):
        board = Board()
        knight = Knight("BLACK", board)
        self.assertEqual(knight.symbol(), 'n')

# testeo movimientos validos

    def test_valid_moves(self):
        """Verifica movimientos válidos en forma de 'L'."""
        valid_moves = [
            ((4, 4), (6, 5)),  # Movimiento en L hacia abajo y derecha
            ((4, 4), (6, 3)),  # Movimiento en L hacia abajo e izquierda
            ((4, 4), (2, 5)),  # Movimiento en L hacia arriba y derecha
            ((4, 4), (2, 3)),  # Movimiento en L hacia arriba e izquierda
            ((4, 4), (5, 6)),  # Movimiento en L hacia la derecha
            ((4, 4), (5, 2)),  # Movimiento en L hacia la izquierda
        ]
        for from_pos, to_pos in valid_moves:
            with self.subTest(from_pos=from_pos, to_pos=to_pos):
                self.assertTrue(self.knight.is_valid_piece_move(self.board, from_pos, to_pos))

# testeo de movimientos invalidos

    def test_invalid_moves(self):
        """Verifica movimientos inválidos que no cumplen la forma de 'L'."""
        invalid_moves = [
            ((4, 4), (4, 6)),  # Movimiento horizontal (no válido para un caballo)
            ((4, 4), (6, 6)),  # Movimiento diagonal (no válido para un caballo)
            ((4, 4), (5, 5)),  # Movimiento recto (no válido para un caballo)
            ((4, 4), (4, 3)),  # Movimiento horizontal (no válido para un caballo)
        ]
        for from_pos, to_pos in invalid_moves:
            with self.subTest(from_pos=from_pos, to_pos=to_pos):
                self.assertFalse(self.knight.is_valid_piece_move(self.board, from_pos, to_pos))


if __name__ == '__main__':
    unittest.main()



















"""
import unittest
from chess.knight import Knight  
from chess.board import Board
from chess.pawn import Pawn

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.board = Board(for_test=True)  # Inicializa el tablero sin piezas
        self.knight = Knight('White', self.board)  # Crea un caballo blanco

# Testeo de las posiciones posibles
    def test_get_possible_positions(self):
        self.board.set_piece(3, 3, self.knight) 
        result = self.knight.get_possible_positions(3, 3)
        expected_positions = [
            (5, 4), (5, 2), (1, 4), (1, 2), (4, 5), (4, 1), (2, 5), (2, 1)       # Movimientos en "L"
        ]
        self.assertEqual(result, expected_positions)

# Testeo de los movimientos con una pieza bloqueando

    def test_get_possible_positions_with_block(self):
        self.board.set_piece(3, 3, self.knight)  
        self.board.set_piece(5, 4, Pawn('White', self.board))  # Pieza propia bloqueando
        result = self.knight.get_possible_positions(3, 3)
        expected_positions = [
            (5, 2), (1, 4), (1, 2), (4, 5), (4, 1), (2, 5), (2, 1)
        ] 
        self.assertEqual(result, expected_positions)

# Testeo de los movimientos con una pieza enemiga

    def test_get_possible_positions_with_enemy(self):
        self.board.set_piece(3, 3, self.knight)  
        self.board.set_piece(5, 4, Pawn('Black', self.board))  # Pieza enemiga en (5, 4)
        result = self.knight.get_possible_positions(3, 3)
        expected_positions = [
            (5, 4), (5, 2), (1, 4), (1, 2), (4, 5), (4, 1), (2, 5), (2, 1)
        ] 
        self.assertEqual(result, expected_positions) # Se puede capturar la pieza enemiga en (5, 4)

# Testeo de los movimientos en "L" en los 4 sentidos (dire)

    def test_knight_moves_in_L(self):
        self.board.set_piece(4, 4, self.knight)       # Coloca el caballo en el centro del tablero (4, 4)
        result = self.knight.get_possible_positions(4, 4)
        
# Movimientos en "L" desde el centro en todas las direcciones posibles
        expected_positions = [
            (6, 5), (6, 3),  # Movimientos en "L" hacia arriba
            (2, 5), (2, 3),  # Movimientos en "L" hacia abajo
            (5, 6), (5, 2),  # Movimientos en "L" hacia la derecha
            (3, 6), (3, 2)   # Movimientos en "L" hacia la izquierda
        ]
        self.assertEqual(result, expected_positions)




if __name__ == '__main__':
    unittest.main()

"""
