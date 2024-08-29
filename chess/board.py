from chess.rook import Rook
from chess.knight import Knight
from chess.bishop import Bishop
from chess.queen import Queen
from chess.king import King
from chess.pawn import Pawn

class Board:                                       #se crea un tablero de ajedrez vacío de 8x8 y coloca todas las piezas en sus posiciones iniciales, con piezas negras en la primera fila y piezas blancas en la última fila
    def __init__(self, for_test = False):
        self.__positions__ = []                      #matriz (lista de listas)
        for _ in range(8):                           #por cada fila creo una columna con ocho lugares
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        if not for_test:                          #indica si el tablero se está inicializando para una prueba (test unitario) o para el juego normal
            
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
    
    def __str__(self):                         #convierte el tablero en una cadena de texto que muestra las piezas en sus posiciones, dejando espacios en blanco donde no hay piezas, para que puedas ver el tablero en la consola.
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str
    
    def get_piece(self, row, col):             #devuelve la pieza que se encuentra en una posición específica del tablero. Toma como parámetros la fila (row) y la columna (col) y devuelve la pieza ubicada en esa celda, o None si la celda está vacía.
            return self.__positions__ [row] [col]
    
    def set_piece(self, row, col, piece):      #mueve una pieza en una posición específica del tablero al actualizar las posiciones
        self.__positions__[row][col] = piece