from pieces import Rook
from pieces import Bishop

    class Board:
        def _init__ (self):
            self.__positions__ = [] #matriz (lista de listas)
            for _ in range(8):  #por cada fila creo una columna con ocho lugares
                col = []
                for _ in range(8):
                    col.append(None)
                self.__positions__.append(col)
            
            self.__positions__[0] [0] = Rook('Black') #torres negra
            self.__positions__[7] [7] = Rook('White') #torre blanca
            self.__positions__[0] [7] = Rook('Black') #torres negra2
            self.__positions__[7] [0] = Rook('White') #torre blanca2
            self.__positions__[0] [2] = Bishop('Black') #alfil negro
            self.__positions__[0] [5] = Bishop('Black') #alfil negro2
            self.__positions__[7] [2] = Bishop('White') #alfil blanco
            self.__positions__[7] [5] = Bishop('White') #alfil blanco2

        def get_piece(self, row, col):
            return self.__positions__ [row] [col]
