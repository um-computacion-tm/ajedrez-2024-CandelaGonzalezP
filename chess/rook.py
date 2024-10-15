from chess.pieces import Piece       #TORRE

class Rook(Piece):

    """
    Clase que representa una torre en el juego de ajedrez.

    Hereda de la clase Piece, lo que proporciona las funcionalidades básicas 
    para las piezas del juego.
    """

    def symbol(self):
        return '♖' if self.get_color() == 'WHITE' else '♜'


# Movimientos ortogonales

    def rook_valid_positions(self, from_row, from_col, to_row, to_col):

        """
        Verifica si el movimiento de la torre es válido.

        Args:
            from_row (int): Fila de origen de la torre.
            from_col (int): Columna de origen de la torre.
            to_row (int): Fila de destino de la torre.
            to_col (int): Columna de destino de la torre.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.

        Description:
            Esta función verifica si el movimiento de la torre desde (from_row, from_col) 
            hasta (to_row, to_col) es válido, considerando sus movimientos ortogonales (arriba, 
            abajo, izquierda, derecha).
        """

        directions = self.get_rook_directions()
        possible_positions = self.find_valid_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions

    def get_rook_directions(self):

        """
        Obtiene las direcciones válidas en las que la torre puede moverse.

        Returns:
            list: Lista de tuplas que representan las direcciones ortogonales (arriba, abajo, izquierda, derecha).
        """

        return [(1, 0), (-1, 0), (0, -1), (0, 1)]