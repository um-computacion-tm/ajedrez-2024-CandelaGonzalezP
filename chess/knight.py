from chess.pieces import Piece      #CABALLO 

class Knight(Piece):
        
    """
    Clase que representa un caballo en el juego de ajedrez.
    
    Hereda de la clase Piece, lo que proporciona las funcionalidades básicas 
    para las piezas del juego.
    """

    def symbol(self):

        """
        Obtiene el símbolo que representa al caballo.

        Returns:
            str: El símbolo del caballo en función de su color ("♘" para blancas, "♞" para negras).
        """

        return '♘' if self.get_color() == 'WHITE' else '♞' 

# Movimientos en L en toda direccion

    def valid_positions(self, from_row, from_col, to_row, to_col):

        """
        Verifica si el movimiento del caballo es válido.

        Args:
            from_row (int): Fila de la posición de origen.
            from_col (int): Columna de la posición de origen.
            to_row (int): Fila de la posición de destino.
            to_col (int): Columna de la posición de destino.

        Returns:
            bool: True si el movimiento es válido, False de lo contrario.
        """

        valid_moves = self.get_possible_moves(from_row, from_col)
        if (to_row, to_col) not in valid_moves:
            return False
        return True  

    def get_possible_moves(self, from_row, from_col):

        """
        Obtiene las posiciones válidas a las que el caballo puede moverse.

        Args:
            from_row (int): Fila de la posición inicial.
            from_col (int): Columna de la posición inicial.

        Returns:
            list: Lista de posiciones válidas a las que el caballo puede moverse.
        """

        knight_moves = [
            (from_row + 2, from_col + 1), (from_row + 2, from_col - 1),
            (from_row - 2, from_col + 1), (from_row - 2, from_col - 1),
            (from_row + 1, from_col + 2), (from_row + 1, from_col - 2),
            (from_row - 1, from_col + 2), (from_row - 1, from_col - 2)
        ]
        return knight_moves