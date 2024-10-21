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
        # Piezas negras en la fila 0
        self.setup_piece(Rook, [(0, 0), (0, 7)])  # Torres negras
        self.setup_piece(Knight, [(0, 1), (0, 6)])  # Caballos negros
        self.setup_piece(Bishop, [(0, 2), (0, 5)])  # Alfiles negros
        self.setup_piece(Queen, [(0, 3)])  # Reina negra
        self.setup_piece(King, [(0, 4)])  # Rey negro
        
        # Piezas blancas en la fila 7
        self.setup_piece(Rook, [(7, 0), (7, 7)])  # Torres blancas
        self.setup_piece(Knight, [(7, 1), (7, 6)])  # Caballos blancos
        self.setup_piece(Bishop, [(7, 2), (7, 5)])  # Alfiles blancos
        self.setup_piece(Queen, [(7, 3)])  # Reina blanca
        self.setup_piece(King, [(7, 4)])  # Rey blanco
        
        self.setup_pawns()  # Peones

    def setup_piece(self, piece_class, positions):
        for position in positions:
            if position[0] == 0:
                color = "BLACK"  # Piezas negras en la fila 0
            elif position[0] == 7:
                color = "WHITE"  # Piezas blancas en la fila 7
            else:
                continue  # Si no es una fila válida, omite esta posición.
            self.__positions__[position[0]][position[1]] = piece_class(color, self)

    def setup_pawns(self):
        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK", self)  # Peones negros
            self.__positions__[6][col] = Pawn("WHITE", self)  # Peones blancos

    def __str__(self):
        board_str = "  0 1 2 3 4 5 6 7\n"  # Índices de columna
        for row in range(8):  # Recorre las filas de 0 a 7
            row_str = f"{row} "  # Agrega el número de fila al principio
            for col in range(8):
                piece = self.get_piece(row, col)  # Obtén la pieza en la posición
                row_str += self.get_cell_string(piece) + " "  # Espacio después de cada pieza
            board_str += row_str.strip() + "\n"  # Agrega la fila al tablero
        return board_str.strip()  # Elimina el último salto de línea

    def get_cell_string(self, cell):
        return cell.symbol() if cell is not None else "."
    
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