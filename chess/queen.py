from chess.pieces import Piece        # REINA

class Queen(Piece):
    
    """
    Clase que representa una reina en el juego de ajedrez.
    
    Hereda de la clase Piece, lo que proporciona las funcionalidades básicas 
    para las piezas del juego.
    """

    def symbol(self):

        """
        Obtiene el símbolo que representa a la reina en el tablero.

        Returns:
            str: Símbolo de la reina en función de su color.
        """

        return '♕' if self.get_color() == 'WHITE' else '♛'

# Movimientos en diagonal y ortogonales

    def valid_positions(self, from_row, from_col, to_row, to_col):

        """
        Verifica si el movimiento de la reina es válido.

        Args:
            from_row (int): Fila de la posición de origen.
            from_col (int): Columna de la posición de origen.
            to_row (int): Fila de la posición de destino.
            to_col (int): Columna de la posición de destino.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """

        return self._is_valid_move(from_row, from_col, to_row, to_col)

    def _is_valid_move(self, from_row, from_col, to_row, to_col):

        """
        Determina si el movimiento de la reina hacia una posición específica es válido.

        Args:
            from_row (int): Fila de la posición de origen.
            from_col (int): Columna de la posición de origen.
            to_row (int): Fila de la posición de destino.
            to_col (int): Columna de la posición de destino.

        Returns:
            bool: True si la posición de destino es válida para el movimiento de la reina, 
                  False en caso contrario.
        """

        directions = self._king_queen_directions_
        possible_positions = self.get_possible_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions

    def get_possible_moves(self, from_row, from_col, directions):

        """
        Obtiene las posiciones válidas de la reina desde una posición inicial.

        Args:
            from_row (int): Fila de la posición de origen.
            from_col (int): Columna de la posición de origen.
            directions (list): Lista de direcciones de movimiento válidas.

        Returns:
            list: Lista de posiciones a las que la reina puede moverse.
        """

        return self.find_valid_moves(from_row, from_col, directions, single_step=False)