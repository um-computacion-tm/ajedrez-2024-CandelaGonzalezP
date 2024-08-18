from pieces import Piece       #TORRE CLASE

class Rook (Piece):
    ...

    def __init__(self, position):
        self.__position__ = position

    def can_move(self, new_position):
        return (self.__position__[0] == new_position[0] or self.__position__[1] == new_position[1])     # La torre se mueve en la misma fila o columna
    
import unittest

class TestRook(unittest.TestCase):

    def test_move_right(self):                #mueve la torre hacia la derecha (fila)
        rook = Rook((0, 0))
        result = rook.can_move((0, 5))
        self.assertEqual(result, True)

    def test_move_down(self):                 #mueve la torre hacia la izquierda (columna)
        rook = Rook((0, 0))
        result = rook.can_move((5, 0))
        self.assertEqual(result, True)

    def test_move_diagonal_1(self):
        rook = Rook((0, 0))                   #mueve la torre hacia las diagonales (invalido)
        result = rook.can_move((1, 1))
        self.assertEqual(result, False)

    def test_move_diagonal_2(self):
        rook = Rook((0, 0))
        result = rook.can_move((5, 5))
        self.assertEqual(result, False)

    def test_move_diagonal_3(self):
        rook = Rook((0, 0))
        result = rook.can_move((7, 7))
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()

