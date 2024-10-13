from chess.rook import Rook
from chess.knight import Knight
from chess.bishop import Bishop
from chess.queen import Queen
from chess.king import King
from chess.pawn import Pawn
from chess.exceptions import *

class Board:                                       #se crea un tablero vacío de 8x8 y coloca piezas en sus posiciones iniciales, con piezas negras en la primera fila y piezas blancas en la última fila
    
    def __init__(self, for_test=False):
        self.__positions__ = self.initialize_board()
        if not for_test:
            self.setup_pieces()

    def initialize_board(self):
        """Crea una matriz 8x8 inicializada con None."""
        return [[None for _ in range(8)] for _ in range(8)]
    
    def setup_pieces(self):
        """Configura las piezas en el tablero."""
        self.setup_piece(Rook, ['Black', 'White'], [(0, 0), (0, 7), (7, 0), (7, 7)])  # Torres
        self.setup_piece(Bishop, ['Black', 'White'], [(0, 2), (0, 5), (7, 2), (7, 5)])  # Alfiles
        self.setup_piece(King, ['Black', 'White'], [(0, 4), (7, 4)])  # Reyes
        self.setup_piece(Queen, ['Black', 'White'], [(0, 3), (7, 3)])  # Reinas
        self.setup_piece(Knight, ['Black', 'White'], [(0, 1), (0, 6), (7, 1), (7, 6)])  # Caballos
        self.setup_pawns()  # Peones

    def setup_piece(self, piece_class, colors, positions):
        """Coloca piezas en el tablero."""
        for i, position in enumerate(positions):
            color = colors[i // 2]  # Alterna entre 'Black' y 'White'
            self.__positions__[position[0]][position[1]] = piece_class(color, self)

    def setup_pawns(self):
        """Coloca los peones en el tablero."""
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK", self)  # Peones negros
            self.__positions__[6][col] = Pawn("WHITE", self)  # Peones blancos



    
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
        """Cuenta el número de piezas de un color específico en el tablero."""
        count = 0
        for row in self.__positions__:
            count += self.count_color_in_row(row, color)
        return count

    def count_color_in_row(self, row, color):
        """Cuenta el número de piezas del color específico en una fila."""
        count = 0
        for piece in row:
            if self.is_piece_color(piece, color):
                count += 1
        return count

    def is_piece_color(self, piece, color):
        """Verifica si la pieza no es None y si su color coincide con el color especificado."""
        return piece is not None and piece.get_color() == color



    """def count_pieces(self, color):
        count = 0
        for row in self.__positions__:
            for piece in row:
                if piece is not None and piece.get_color() == color:
                    count += 1
        return count"""