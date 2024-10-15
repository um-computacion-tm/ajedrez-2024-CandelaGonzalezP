from chess.pieces import Piece                 #ALFIL

class Bishop(Piece):

    """
    Clase que representa un alfil en el juego de ajedrez.
    
    Hereda de la clase Piece, lo que proporciona las funcionalidades básicas 
    para las piezas del juego.
    """

    def symbol(self):
        return '♗' if self.get_color() == 'WHITE' else '♝'


# Movimientos en diagonal

    def bishop_valid_position(self, from_row, from_col, to_row, to_col):

        """
        Verifica si el movimiento del alfil es válido.

        Args:
            from_row (int): Fila de la posición inicial del alfil.
            from_col (int): Columna de la posición inicial del alfil.
            to_row (int): Fila de la posición final a la que se desea mover el alfil.
            to_col (int): Columna de la posición final a la que se desea mover el alfil.

        Returns:
            bool: True si el movimiento es válido (diagonal), False en caso contrario.
        
        Description:
            Esta función verifica si el movimiento desde (from_row, from_col) 
            a (to_row, to_col) es diagonal y si la posición final está dentro 
            de las posiciones posibles que puede alcanzar el alfil.
            El alfil se mueve en diagonales y su comportamiento se basa en 
            la implementación de la clase base Piece.
        """

        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        possible_positions = self.find_valid_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions
