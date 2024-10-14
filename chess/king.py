from chess.pieces import Piece        #REY 

class King(Piece):

    """
    Clase que representa un rey en el juego de ajedrez.
    
    Hereda de la clase Piece, lo que proporciona las funcionalidades básicas 
    para las piezas del juego.
    """

    def symbol(self):

        """
        Obtiene el símbolo que representa al rey según su color.

        Returns:
            str: 'K' si el rey es blanco, 'k' si es negro.
        """

        return 'K' if self.get_color() == "WHITE" else 'k'

# Movimientos de a una casilla en todas las direcciones

    def king_valid_position(self, from_row, from_col, to_row, to_col):

        """
        Verifica si el movimiento del rey es válido.

        Args:
            from_row (int): Fila de la posición inicial del rey.
            from_col (int): Columna de la posición inicial del rey.
            to_row (int): Fila de la posición final a la que se desea mover el rey.
            to_col (int): Columna de la posición final a la que se desea mover el rey.

        Returns:
            bool: True si el movimiento es válido (una casilla en cualquier dirección), False en caso contrario.
        
        Description:
            Esta función verifica si el movimiento desde (from_row, from_col) 
            a (to_row, to_col) es válido para el rey, que puede moverse solo 
            una casilla en cualquier dirección. Se utilizan las direcciones 
            válidas del rey definidas en la clase base Piece.
        """

        directions = self.__king_queen_directions__
        possible_positions = self.find_valid_moves(from_row, from_col, directions, single_step=True)
        return (to_row, to_col) in possible_positions
