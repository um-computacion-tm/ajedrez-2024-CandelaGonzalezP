import unittest
from chess.rook import Rook
from chess.board import Board

class TestRookInitialization(unittest.TestCase):

    def test_rook_initialization(self):
        position = (4, 4)                                             #Prueba que la torre se inicializa con la posición y el color correctos.
        color = 'White'
        rook = Rook(position, color)
        self.assertEqual(rook.__position__, position)                 # Verificar que la posición se ha establecido correctamente
        self.assertEqual(rook._Rook__color__, color)                  # Verificar que el color se ha establecido correctamente
    
    
    def test_rook_position_and_color(self):
        position = (2, 3)                                             #Prueba que la posición y el color son los esperados después de la inicialización.
        color = 'Black'
        rook = Rook(position, color)
        self.assertEqual(rook.__position__, position)                  # Verificar que la posición es la correcta
        self.assertEqual(rook._Rook__color__, color)                   # Verificar que el color es el correcto


class TestRook(unittest.TestCase):
    
    def test_rook_white_str(self):
        rook = Rook((0, 0), 'White')                                   #Prueba que el método __str__ devuelva el símbolo correcto para una torre blanca.
        self.assertEqual(str(rook), "♖")

    def test_rook_black_str(self):
        rook = Rook((0, 0), 'Black')                                    #Prueba que el método __str__ devuelva el símbolo correcto para una torre negra.
        self.assertEqual(str(rook), "♜")




class TestRook(unittest.TestCase):
    def setUp(self):
        self.board = Board()                                               #Configura el tablero y las torres para las pruebas.
        
    def test_moves_forward(self):
        rook = Rook((0, 0), 'Black')                                       #Prueba los movimientos hacia adelante de una torre.
        moves = rook.get_possible_moves(self.board)
        expected_moves = [(i, 0) for i in range(1, 8)]                     # Movimiento vertical hacia abajo
        self.assertTrue(all(move in moves for move in expected_moves))

    def test_moves_backward(self):
        rook = Rook((7, 0), 'White')                                         #Prueba los movimientos hacia atrás de una torre.
        moves = rook.get_possible_moves(self.board)
        expected_moves = [(i, 0) for i in range(0, 7)]                        # Movimiento vertical hacia arriba
        self.assertTrue(all(move in moves for move in expected_moves))

    def test_moves_left(self):
        rook = Rook((0, 7), 'Black')                                         #Prueba los movimientos hacia la izquierda de una torre.
        moves = rook.get_possible_moves(self.board)
        expected_moves = [(0, j) for j in range(0, 6)]                        # Movimiento horizontal hacia la izquierda
        self.assertTrue(all(move in moves for move in expected_moves))

    def test_moves_right(self):
        rook = Rook((0, 0), 'White')                                          #Prueba los movimientos hacia la derecha de una torre.
        moves = rook.get_possible_moves(self.board)
        expected_moves = [(0, j) for j in range(1, 8)]                        # Movimiento horizontal hacia la derecha
        self.assertTrue(all(move in moves for move in expected_moves))

    def test_moves_diagonal(self):
        rook = Rook((4, 4), 'Black')                                           #Prueba que la torre no pueda moverse en diagonal.
        moves = rook.get_possible_moves(self.board)
        diagonal_moves = [(i, i) for i in range(8)]                            # Posiciones diagonales en el tablero
        self.assertTrue(all(move not in moves for move in diagonal_moves))

if __name__ == '__main__':
    unittest.main()
