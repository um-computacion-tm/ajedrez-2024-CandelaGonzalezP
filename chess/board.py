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

    def __init__(self):

        """
        Inicializa el tablero de ajedrez como una matriz de 8x8 con valores
        None en todas las posiciones, e invoca el método `setup_pieces` 
        para colocar las piezas en sus posiciones iniciales.
        """

        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):

        """
        Coloca las piezas de ajedrez en sus posiciones iniciales.
        
        Las piezas negras se colocan en las filas 0 y 1, mientras que las 
        piezas blancas se colocan en las filas 6 y 7.
        """

# piezas negras

        self.__positions__[0][0] = Rook('BLACK', self)
        self.__positions__[0][1] = Knight('BLACK', self)
        self.__positions__[0][2] = Bishop('BLACK', self)
        self.__positions__[0][3] = Queen('BLACK', self)
        self.__positions__[0][4] = King('BLACK', self)
        self.__positions__[0][5] = Bishop('BLACK', self)
        self.__positions__[0][6] = Knight('BLACK', self)
        self.__positions__[0][7] = Rook('BLACK', self)

        for i in range(8):
            self.__positions__[1][i] = Pawn('BLACK', self)

# piezas blancas

        self.__positions__[7][0] = Rook('WHITE', self)
        self.__positions__[7][1] = Knight('WHITE', self)
        self.__positions__[7][2] = Bishop('WHITE', self)
        self.__positions__[7][3] = Queen('WHITE', self)
        self.__positions__[7][4] = King('WHITE', self)
        self.__positions__[7][5] = Bishop('WHITE', self)
        self.__positions__[7][6] = Knight('WHITE', self)
        self.__positions__[7][7] = Rook('WHITE', self)

        for i in range(8):
            self.__positions__[6][i] = Pawn('WHITE', self)

    def __str__(self):

        """
        Convierte el estado actual del tablero en una cadena de texto
        que muestra las posiciones de las piezas.

        Returns:
            str: Representación visual del tablero con números de fila y columna.
        """

        return self.build_board_string()
    
    def build_board_string(self):

        """
        Construye una cadena de texto que representa el estado actual del tablero,
        con los símbolos de las piezas y las posiciones vacías.

        Returns:
            str: Representación del tablero de ajedrez con los símbolos de las piezas.
        """

        board_str = "   0  1  2  3  4  5  6  7\n"  
        for i, row in enumerate(self.__positions__):
            board_str += f"{i}  " 
            for cell in row:
                board_str += self.get_cell_string(cell) + "  "
            board_str += "\n"
        return board_str
    
    def get_cell_string(self, cell):

        """
        Devuelve el símbolo de la pieza o un espacio en blanco si la celda está vacía.

        Args:
            cell (Piece or None): La pieza ubicada en una celda del tablero.

        Returns:
            str: El símbolo de la pieza si la celda está ocupada, un espacio en blanco si está vacía.
        """

        return cell.symbol() if cell is not None else " "
    

    def get_piece(self, row, col):

        """
        Obtiene la pieza en una posición específica del tablero.

        Args:
            row (int): La fila de la posición en el tablero.
            col (int): La columna de la posición en el tablero.

        Returns:
            Piece or None: La pieza en la posición dada, o None si no hay ninguna pieza.

        Raises:
            OriginInvalidMove: Si la posición especificada está fuera de los límites del tablero.
        """

        if not (0 <= row < 8 and 0 <= col < 8):
         raise OriginInvalidMove()
        return self.__positions__[row][col]
    
    def set_piece(self, row, col, piece):

        """
        Coloca una pieza en una posición específica del tablero.

        Args:
            row (int): La fila de la posición en el tablero.
            col (int): La columna de la posición en el tablero.
            piece (Piece or None): La pieza que se va a colocar en la posición. Puede ser None para vaciar la celda.
        """

        self.__positions__[row][col] = piece

    def move(self, from_row, from_col, to_row, to_col):

        """
        Mueve una pieza de una posición a otra en el tablero.

        Args:
            from_row (int): La fila de la posición de origen.
            from_col (int): La columna de la posición de origen.
            to_row (int): La fila de la posición de destino.
            to_col (int): La columna de la posición de destino.
        """

        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)

    def count_pieces(self, color):

        """
        Cuenta cuántas piezas de un color específico están en el tablero.

        Args:
            color (str): El color de las piezas a contar ('WHITE' o 'BLACK').

        Returns:
            int: El número de piezas del color especificado en el tablero.
        """

        count = 0
        for row in self.__positions__:
            count += self.count_color_in_row(row, color)
        return count
    
    def count_color_in_row(self, row, color):

        """
        Cuenta cuántas piezas de un color específico están en una fila del tablero.

        Args:
            row (list): La fila del tablero donde se realiza el conteo.
            color (str): El color de las piezas a contar ('WHITE' o 'BLACK').

        Returns:
            int: El número de piezas del color especificado en la fila.
        """

        count = 0
        for piece in row:
            if self.is_piece_color(piece, color):
                count += 1
        return count
    
    def is_piece_color(self, piece, color):

        """
        Verifica si una pieza es de un color específico.

        Args:
            piece (Piece or None): La pieza a verificar.
            color (str): El color a verificar ('WHITE' o 'BLACK').

        Returns:
            bool: True si la pieza es del color especificado, False en caso contrario.
        """

        return piece is not None and piece.get_color() == color