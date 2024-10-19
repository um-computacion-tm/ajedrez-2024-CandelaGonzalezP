from chess.rook import Rook
from chess.knight import Knight
from chess.bishop import Bishop
from chess.queen import Queen
from chess.king import King
from chess.pawn import Pawn
from chess.exceptions import *

class Board:                                       
    
    """
    Clase que representa el tablero de ajedrez.

    Esta clase se encarga de inicializar el tablero, colocar las piezas y 
    gestionar su estado.
    """

    def __init__(self, for_test=False):
        self.__positions__ = self.initialize_board()
        if not for_test:
            self.setup_pieces()

    def initialize_board(self):
        return [[None for _ in range(8)] for _ in range(8)]
    
    def setup_pieces(self):
        self.setup_piece(Rook, ['BLACK', 'WHITE'], [(0, 0), (0, 7), (7, 0), (7, 7)])  # Torres
        self.setup_piece(Bishop, ['BLACK', 'WHITE'], [(0, 2), (0, 5), (7, 2), (7, 5)])  # Alfiles
        self.setup_piece(King, ['BLACK', 'WHITE'], [(0, 4), (7, 4)])  # Reyes
        self.setup_piece(Queen, ['BLACK', 'WHITE'], [(0, 3), (7, 3)])  # Reinas
        self.setup_piece(Knight, ['BLACK', 'WHITE'], [(0, 1), (0, 6), (7, 1), (7, 6)])  # Caballos
        self.setup_pawns()  # Peones

    def setup_piece(self, piece_class, colors, positions):
        for i, position in enumerate(positions):
            color = colors[i // 2]  # Alterna entre 'Black' y 'White'
            self.__positions__[position[0]][position[1]] = piece_class(color, self)

    def setup_pawns(self):
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK", self)  # Peones negros
            self.__positions__[6][col] = Pawn("WHITE", self)  # Peones blancos



    def __str__(self):  
        return self.build_board_string()



    def build_board_string(self):
        board_str = "  0 1 2 3 4 5 6 7\n"  # Índices de columna
        for i, row in enumerate(self.__positions__):
            board_str += f"{i} "  # Índice de fila
            for cell in row:
                board_str += self.get_cell_string(cell) + " "
            board_str += "\n"
        return board_str



    def get_cell_string(self, cell):
        return cell.symbol() if cell is not None else " " 



    def get_piece(self, row, col):
        if not (0 <= row < 8 and 0 <= col < 8):
         raise OriginInvalidMove()
        return self.__positions__[row][col]
    

    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece


    def move(self, from_row, from_col, to_row, to_col):
        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)

    def count_pieces(self, color):
        count = 0
        for row in self.__positions__:
            count += self.count_color_in_row(row, color)
        return count

    def count_color_in_row(self, row, color):
        count = 0
        for piece in row:
            if self.is_piece_color(piece, color):
                count += 1
        return count

    def is_piece_color(self, piece, color):
        return piece is not None and piece.get_color() == color   
    






