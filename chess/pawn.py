from chess.pieces import Piece             #PEON
from chess.queen import Queen

class Pawn(Piece):
    
    """
    Clase que representa peones en el juego de ajedrez.
    
    Hereda de la clase Piece, lo que proporciona las funcionalidades básicas 
    para las piezas del juego.
    """

    def __init__(self, color, board):

        """
        Inicializa un peón con su color y el tablero en el que se encuentra.

        Args:
            color (str): El color del peón ("WHITE" o "BLACK").
            board (Board): El tablero donde se encuentra el peón.
        """

        super().__init__(color, board)  

    def symbol(self):

        """
        Obtiene el símbolo que representa al peón.

        Returns:
            str: El símbolo del peón en función de su color ("♙" para blancas, "♟" para negras).
        """

        return '♙' if self.get_color() == 'WHITE' else '♟'

    def valid_positions(self, from_row, from_col, to_row, to_col):

        """
        Verifica si el movimiento del peón es válido.

        Args:
            from_row (int): Fila de la posición de origen.
            from_col (int): Columna de la posición de origen.
            to_row (int): Fila de la posición de destino.
            to_col (int): Columna de la posición de destino.

        Returns:
            bool: True si el movimiento es válido, False de lo contrario.
        """

        possible_moves = self.get_possible_moves(from_row, from_col)
        return any(move == (to_row, to_col) for move in possible_moves)
        
    def get_possible_moves(self, from_row, from_col):

        """
        Obtiene las posiciones válidas a las que el peón puede moverse.

        Args:
            from_row (int): Fila de la posición inicial.
            from_col (int): Columna de la posición inicial.

        Returns:
            list: Lista de posiciones válidas a las que el peón puede moverse.
        """

        moves = []
        direction = self.get_move_direction() 
        start_row = self.get_start_row()      

        # Movimientos hacia adelante
        self.add_forward_moves(from_row, from_col, direction, moves)

        # Capturas diagonales
        self.add_capture_moves(from_row, from_col, direction, moves)

        return moves

    def add_forward_moves(self, from_row, from_col, direction, moves):

        """
        Agrega los movimientos hacia adelante del peón a la lista de movimientos.

        Args:
            from_row (int): Fila de la posición inicial.
            from_col (int): Columna de la posición inicial.
            direction (int): Dirección en la que se mueve el peón (-1 para blanco, 1 para negro).
            moves (list): Lista donde se agregarán los movimientos válidos.
        """

        start_row = self.get_start_row()
        if self.is_empty(from_row + direction, from_col):
            moves.append((from_row + direction, from_col))
            if from_row == start_row and self.is_empty(from_row + 2 * direction, from_col):
                moves.append((from_row + 2 * direction, from_col))

    def add_capture_moves(self, from_row, from_col, direction, moves):

        """
        Agrega las capturas diagonales del peón a la lista de movimientos.

        Args:
            from_row (int): Fila de la posición inicial.
            from_col (int): Columna de la posición inicial.
            direction (int): Dirección en la que se mueve el peón (-1 para blanco, 1 para negro).
            moves (list): Lista donde se agregarán los movimientos válidos.
        """

        capture_moves = [(direction, -1), (direction, 1)]
        for move in capture_moves:
            next_row, next_col = from_row + move[0], from_col + move[1]
            if self.is_in_bounds(next_row, next_col) and self.can_capture(next_row, next_col):
                moves.append((next_row, next_col))

    def get_move_direction(self):

        """
        Obtiene la dirección en la que se mueve el peón.

        Returns:
            int: -1 si el peón es blanco, 1 si el peón es negro.
        """

        return -1 if self.get_color() == 'WHITE' else 1

    def get_start_row(self):

        """
        Obtiene la fila de inicio del peón según su color.

        Returns:
            int: 6 si el peón es blanco, 1 si el peón es negro.
        """

        return 6 if self.get_color() == 'WHITE' else 1 

    def is_in_bounds(self, row, col):

        """
        Verifica si la posición está dentro de los límites del tablero.

        Args:
            row (int): Fila a verificar.
            col (int): Columna a verificar.

        Returns:
            bool: True si la posición está dentro de los límites, False de lo contrario.
        """

        return 0 <= row < 8 and 0 <= col < 8

    def is_empty(self, row, col):

        """
        Verifica si una casilla está vacía.

        Args:
            row (int): Fila de la posición a verificar.
            col (int): Columna de la posición a verificar.

        Returns:
            bool: True si la casilla está vacía, False de lo contrario.
        """

        return self.is_in_bounds(row, col) and self.__board__.get_piece(row, col) is None

    def can_capture(self, row, col):

        """
        Verifica si el peón puede capturar una pieza en la posición especificada.

        Args:
            row (int): Fila de la posición a verificar.
            col (int): Columna de la posición a verificar.

        Returns:
            bool: True si el peón puede capturar, False de lo contrario.
        """

        piece = self.__board__.get_piece(row, col)
        return piece is not None and piece.get_color() != self.get_color() 