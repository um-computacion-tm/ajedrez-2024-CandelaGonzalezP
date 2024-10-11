from chess.rook import Rook
from chess.knight import Knight
from chess.bishop import Bishop
from chess.queen import Queen
from chess.king import King
from chess.pawn import Pawn
from chess.exceptions import *

class Board:

    def __init__(self, for_test=False):
        self.__positions__ = self.initialize_empty_board()
        if not for_test:
            self.setup_initial_positions()

    def initialize_empty_board(self):
        """Inicializa un tablero vacío de 8x8."""
        return [[None for _ in range(8)] for _ in range(8)]

    def setup_initial_positions(self):
        """Configura las posiciones iniciales de las piezas en el tablero."""
        self.set_rooks()
        self.set_bishops()
        self.set_king_and_queen()
        self.set_knights()
        self.set_pawns()

    def set_rooks(self):
        """Coloca las torres en sus posiciones iniciales."""
        self.__positions__[0][0] = Rook('Black', self)
        self.__positions__[7][0] = Rook('White', self)
        self.__positions__[0][7] = Rook('Black', self)
        self.__positions__[7][7] = Rook('White', self)

    def set_bishops(self):
        """Coloca los alfiles en sus posiciones iniciales."""
        self.__positions__[0][2] = Bishop('Black', self)
        self.__positions__[0][5] = Bishop('Black', self)
        self.__positions__[7][2] = Bishop('White', self)
        self.__positions__[7][5] = Bishop('White', self)

    def set_king_and_queen(self):
        """Coloca el rey y la reina en sus posiciones iniciales."""
        self.__positions__[0][4] = King('Black', self)
        self.__positions__[7][4] = King('White', self)
        self.__positions__[0][3] = Queen('Black', self)
        self.__positions__[7][3] = Queen('White', self)

    def set_knights(self):
        """Coloca los caballos en sus posiciones iniciales."""
        self.__positions__[0][1] = Knight('Black', self)
        self.__positions__[0][6] = Knight('Black', self)
        self.__positions__[7][1] = Knight('White', self)
        self.__positions__[7][6] = Knight('White', self)

    def set_pawns(self):
        """Coloca los peones en sus posiciones iniciales."""
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK", self)
            self.__positions__[6][col] = Pawn("WHITE", self)


    """def __init__(self, for_test = False):
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

            for col in range(8):
                self.__positions__[1][col]= Pawn("BLACK", self) #peones negros
                self.__positions__[6][col]= Pawn("WHITE", self) #peones blancos"""

    def __str__(self):
        """Convierte el tablero en una cadena de texto mostrando las piezas en sus posiciones."""
        rows = [self.get_row_string(row) for row in self.__positions__]
        return "\n".join(rows)

    def get_row_string(self, row):
        """Devuelve una representación en cadena de una fila del tablero."""
        return " ".join(self.get_cell_string(cell) for cell in row)

    def get_cell_string(self, cell):
        """Devuelve una representación en cadena de una celda del tablero."""
        if cell is not None:
            return str(cell)  # Representación de la pieza
        return "."  # Representación de una celda vacía

    
    """def __str__(self):                         #convierte el tablero en una cadena de texto que muestra las piezas en sus posiciones, dejando espacios en blanco donde no hay piezas, para que puedas ver el tablero en la consola.
        board_str = ""
        for row in self.__positions__:
            for cell in row:
                if cell is not None:
                    board_str += str(cell)
                else:
                    board_str += " "
            board_str += "\n"
        return board_str"""
    
    
    def get_piece(self, row, col):
        if not (0 <= row < 8 and 0 <= col < 8):
         raise OriginInvalidMove()
        return self.__positions__[row][col]
    

    def set_piece(self, row, col, piece):      #mueve una pieza en una posición específica del tablero al actualizar las posiciones
        self.__positions__[row][col] = piece


    def move(self, from_row, from_col, to_row, to_col):
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)


    def count_pieces(self, color):
        return sum(
            1 for row in self.__positions__ 
            for piece in row 
            if piece is not None and piece.get_color() == color
        )

    """def count_pieces(self, color):
        count = 0
        for row in self.__positions__:
            for piece in row:
                if piece is not None and piece.get_color() == color:
                    count += 1
        return count"""