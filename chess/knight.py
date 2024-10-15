from chess.pieces import Piece      #CABALLO 

class Knight(Piece):
        
    """
    Clase que representa un caballo en el juego de ajedrez.
    
    Hereda de la clase Piece, lo que proporciona las funcionalidades básicas 
    para las piezas del juego.
    """

    def symbol(self):
        return '♘' if self.get_color() == 'WHITE' else '♞' 

# Movimientos en L en toda direccion

    def knight_valid_position(self, board, from_pos, to_pos):

        """
        Verifica si el movimiento del caballo es válido.

        Args:
            board: El tablero en el que se encuentra el caballo.
            from_pos (tuple): Posición inicial del caballo en el formato (fila, columna).
            to_pos (tuple): Posición final a la que se desea mover el caballo en el formato (fila, columna).

        Returns:
            bool: True si el movimiento es válido (en forma de "L"), False en caso contrario.
        
        Description:
            Esta función verifica si el movimiento desde from_pos a to_pos 
            es válido para el caballo, que se mueve en forma de "L". 
            El movimiento puede ser de 2 casillas en una dirección y 
            1 casilla en la dirección perpendicular, o viceversa.
        """

        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return (abs(from_row - to_row) == 2 and abs(from_col - to_col) == 1) or \
               (abs(from_row - to_row) == 1 and abs(from_col - to_col) == 2)