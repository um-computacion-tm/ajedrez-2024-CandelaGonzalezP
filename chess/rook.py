from pieces import Piece       #TORRE CLASE

class Rook (Piece):
    ...

    def __init__(self, position):
        self.__position__ = position

    def can_move(self, new_position):
        return (self.__position__[0] == new_position[0] or self.__position__[1] == new_position[1])     # La torre se mueve en la misma fila o columna
