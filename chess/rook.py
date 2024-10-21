from chess.pieces import Piece       #TORRE

class Rook(Piece):

    """
    Clase que representa una torre en el juego de ajedrez.

    Hereda de la clase Piece, lo que proporciona las funcionalidades básicas 
    para las piezas del juego.
    """

    def symbol(self):

        """
        Obtiene el símbolo que representa a la torre en el tablero.

        Returns:
            str: Símbolo de la torre en función de su color.
        """

        return '♖' if self.get_color() == 'WHITE' else '♜'


# Movimientos ortogonales


    def valid_positions(self, from_row, from_col, to_row, to_col):

        """
        Verifica si el movimiento de la torre es válido.

        Args:
            from_row (int): Fila de la posición de origen.
            from_col (int): Columna de la posición de origen.
            to_row (int): Fila de la posición de destino.
            to_col (int): Columna de la posición de destino.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.
        """

        possible_moves = self.get_possible_moves(from_row, from_col)
        return (to_row, to_col) in [(move[0], move[1]) for move in possible_moves]  

    def get_possible_moves(self, from_row, from_col):

        """
        Obtiene las posiciones válidas de la torre desde una posición inicial.

        Args:
            from_row (int): Fila de la posición de origen.
            from_col (int): Columna de la posición de origen.

        Returns:
            list: Lista de posiciones a las que la torre puede moverse.
        """

        directions = self.get_rook_directions()
        return self.find_valid_moves(from_row, from_col, directions)

    def get_rook_directions(self):

        """
        Obtiene las direcciones válidas de movimiento de la torre.

        Returns:
            list: Lista de direcciones ortogonales en las que la torre puede moverse.
        """

        return [(1, 0), (-1, 0), (0, -1), (0, 1)]