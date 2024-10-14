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

        """
        Inicializa un nuevo tablero de ajedrez.

        Args:
            for_test (bool): Indica si el tablero es para pruebas. Si es True, 
                             no se configuran las piezas automáticamente.
        """

        self.__positions__ = self.initialize_board()
        if not for_test:
            self.setup_pieces()

    def initialize_board(self):

        """
        Crea una matriz 8x8 inicializada con None.

        Returns:
            list: Una matriz de 8x8 representando el tablero vacío.
        """

        return [[None for _ in range(8)] for _ in range(8)]
    
    def setup_pieces(self):

        """
        Configura las piezas en el tablero.

        Esta función coloca todas las piezas en sus posiciones iniciales 
        al comienzo del juego.
        """

        self.setup_piece(Rook, ['Black', 'White'], [(0, 0), (0, 7), (7, 0), (7, 7)])  # Torres
        self.setup_piece(Bishop, ['Black', 'White'], [(0, 2), (0, 5), (7, 2), (7, 5)])  # Alfiles
        self.setup_piece(King, ['Black', 'White'], [(0, 4), (7, 4)])  # Reyes
        self.setup_piece(Queen, ['Black', 'White'], [(0, 3), (7, 3)])  # Reinas
        self.setup_piece(Knight, ['Black', 'White'], [(0, 1), (0, 6), (7, 1), (7, 6)])  # Caballos
        self.setup_pawns()  # Peones

    def setup_piece(self, piece_class, colors, positions):

        """
        Coloca piezas en el tablero.

        Args:
            piece_class (class): Clase de la pieza a colocar.
            colors (list): Lista de colores de las piezas.
            positions (list): Lista de tuplas con las posiciones iniciales de las piezas.
        """

        for i, position in enumerate(positions):
            color = colors[i // 2]  # Alterna entre 'Black' y 'White'
            self.__positions__[position[0]][position[1]] = piece_class(color, self)

    def setup_pawns(self):

        """
        Coloca los peones en el tablero.

        Esta función coloca los peones en sus posiciones iniciales en las filas 
        1 y 6 del tablero.
        """

        for col in range(8):
            self.__positions__[1][col] = Pawn("BLACK", self)  # Peones negros
            self.__positions__[6][col] = Pawn("WHITE", self)  # Peones blancos


    def __str__(self):  

        """
        Convierte el tablero en una cadena de texto.

        Returns:
            str: Una representación en forma de cadena del tablero y las piezas en sus posiciones.
        """

        return self.build_board_string()

    def build_board_string(self):

        """
        Construye la representación en cadena del tablero.

        Returns:
            str: Una cadena que representa el estado actual del tablero.
        """

        board_str = ""
        for row in self.__positions__:
            board_str += "".join(self.get_cell_string(cell) for cell in row) + "\n"
        return board_str

    def get_cell_string(self, cell):

        """
        Obtiene la representación en cadena de una celda.

        Args:
            cell: La celda del tablero que puede ser una pieza o None.

        Returns:
            str: La representación en cadena de la celda.
        """

        return str(cell) if cell is not None else " "
        

    def get_piece(self, row, col):

        """
        Obtiene la pieza en una posición específica del tablero.

        Args:
            row (int): Fila de la celda.
            col (int): Columna de la celda.

        Returns:
            Piece: La pieza en la posición especificada.

        Raises:
            OriginInvalidMove: Si la posición solicitada está fuera de los límites del tablero.
        """

        if not (0 <= row < 8 and 0 <= col < 8):
         raise OriginInvalidMove()
        return self.__positions__[row][col]
    

    def set_piece(self, row, col, piece):

        """
        Establece una pieza en una posición específica del tablero.

        Args:
            row (int): Fila donde se colocará la pieza.
            col (int): Columna donde se colocará la pieza.
            piece: La pieza a colocar en la posición especificada.
        """

        self.__positions__[row][col] = piece


    def move(self, from_row, from_col, to_row, to_col):

        """
        Mueve una pieza de una posición a otra en el tablero.

        Args:
            from_row (int): Fila de origen de la pieza.
            from_col (int): Columna de origen de la pieza.
            to_row (int): Fila de destino de la pieza.
            to_col (int): Columna de destino de la pieza.
        """

        origin = self.get_piece(from_row, from_col)
        self.set_piece(to_row, to_col, origin)
        self.set_piece(from_row, from_col, None)

    def count_pieces(self, color):

        """
        Cuenta el número de piezas de un color específico en el tablero.

        Args:
            color (str): Color de las piezas a contar.

        Returns:
            int: El número de piezas del color especificado en el tablero.
        """

        count = 0
        for row in self.__positions__:
            count += self.count_color_in_row(row, color)
        return count

    def count_color_in_row(self, row, color):

        """
        Cuenta el número de piezas del color específico en una fila.

        Args:
            row (list): La fila del tablero.
            color (str): Color de las piezas a contar.

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
        Verifica si la pieza es del color especificado.

        Args:
            piece: La pieza a verificar.
            color (str): Color que se está comprobando.

        Returns:
            bool: True si la pieza es del color especificado, False en caso contrario.
        """

        return piece is not None and piece.get_color() == color