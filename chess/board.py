from chess.rook import Rook
from chess.knight import Knight
from chess.bishop import Bishop
from chess.queen import Queen
from chess.king import King
from chess.pawn import Pawn
from chess.exceptions import OutOfBoard

class Board:                                       #se crea un tablero de ajedrez vacío de 8x8 y coloca todas las piezas en sus posiciones iniciales, con piezas negras en la primera fila y piezas blancas en la última fila
    def __init__(self, for_test = False):
        self.__positions__ = []                      #matriz (lista de listas)
        for _ in range(8):                           #por cada fila creo una columna con ocho lugares
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        if not for_test:                          #indica si el tablero se está inicializando para una prueba (test unitario) o para el juego normal
            
            self.__positions__[0] [0] = Rook('Black', self) #torres negra
            self.__positions__[7] [7] = Rook('White', self) #torre blanca
            self.__positions__[0] [7] = Rook('Black', self) #torres negra2
            self.__positions__[7] [0] = Rook('White',self) #torre blanca2
            
            self.__positions__[0] [2] = Bishop('Black', self) #alfil negro
            self.__positions__[0] [5] = Bishop('Black', self) #alfil negro2
            self.__positions__[7] [2] = Bishop('White', self) #alfil blanco
            self.__positions__[7] [5] = Bishop('White', self) #alfil blanco2

            self.__positions__[0][4] = King('Black', self) #rey negro
            self.__positions__[7][4] = King('White', self) #rey blanco

            self.__positions__[0][3] =  Queen('Black', self) #reina negro
            self.__positions__[7][3] = Queen('White', self) #reina blanca

            self.__positions__[0][1] = Knight('Black', self) #caballo negro
            self.__positions__[0][6] = Knight ('Black', self) #caballo negro2
            self.__positions__[7][1] = Knight ('White', self) #caballo blanco
            self.__positions__[7][6] = Knight ('White', self) #caballo blanco2

            for i in range(8):
                self.__positions__[1][i] = Pawn("Black", self)  #peones negros
                self.__positions__[6][i] = Pawn("White", self)  #peones blancos
    
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
    
    def get_piece(self, row, col):
        if not (
            0 <= row < 8 or 0 <= col < 8
        ):
            raise OutOfBoard()
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):      #mueve una pieza en una posición específica del tablero al actualizar las posiciones
        self.__positions__[row][col] = piece


    def move(self, from_row, from_col, to_row, to_col):
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)