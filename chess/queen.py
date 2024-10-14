from chess.pieces import Piece         #REINA

class Queen(Piece):
    
    """
    Clase que representa una reina en el juego de ajedrez.
    
    Hereda de la clase Piece, lo que proporciona las funcionalidades básicas 
    para las piezas del juego.
    """

    def symbol(self):

        """
        Obtiene el símbolo que representa a la reina según su color.

        Returns:
            str: 'Q' si la reina es blanca, 'q' si es negra.
        """

        return 'Q' if self.get_color() == "WHITE" else 'q'

# Movimientos en diagonal y ortogonales

    def queen_valid_positions(self, move, directions=None):

        """
        Verifica si el movimiento de la reina es válido.

        Args:
            move (dict): Diccionario que contiene las posiciones de origen y destino del movimiento.
                Debe tener las claves 'from_row', 'from_col', 'to_row', y 'to_col'.
            directions (list, optional): Lista de direcciones en las que puede moverse la reina. 
                Si no se proporciona, se utilizan las direcciones predeterminadas de rey/reina.

        Returns:
            bool: True si el movimiento es válido, False en caso contrario.

        Description:
            Esta función verifica si el movimiento de la reina desde (from_row, from_col) 
            hasta (to_row, to_col) es válido, considerando sus movimientos ortogonales y diagonales.
        """

        from_row, from_col, to_row, to_col = move['from_row'], move['from_col'], move['to_row'], move['to_col']
        if directions is None:
            directions = self.__king_queen_directions__
        possible_positions = self.find_valid_moves(from_row, from_col, directions, single_step=False)
        return (to_row, to_col) in possible_positions
