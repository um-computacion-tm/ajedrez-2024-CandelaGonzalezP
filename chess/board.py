from pieces import Rook
from pieces import Bishop
from pieces import Knight
from pieces import King
from pieces import Queen
from pieces import Pawn

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

            self.__positions__[0][4] = King('Black') #rey negro
            self.__positions__[7][4] = King('White') #rey blanco

            self.__positions__[0][3] =  Queen('Black') #reina negro
            self.__positions__[7][3] = Queen('White') #reina blanca

            self.__positions__[0][1] = Knight('Black') #caballo negro
            self.__positions__[0][6] = Knight ('Black') #caballo negro2
            self.__positions__[7][1] = Knight ('White') #caballo blanco
            self.__positions__[7][6] = Knight ('White') #caballo blanco2

        for i in range(8):
            self.__positions__[1][i] = Pawn("BLACK")  #peones negros
            self.__positions__[6][i] = Pawn("WHITE")  #peones blancos

        def get_piece(self, row, col):
            return self.__positions__ [row] [col]