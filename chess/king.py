from chess.pieces import Piece        #REY 

class King(Piece):

    """
    Clase que representa un rey en el juego de ajedrez.
    
    Hereda de la clase Piece, lo que proporciona las funcionalidades básicas 
    para las piezas del juego.
    """

    def symbol(self):
        return '♔' if self.get_color() == 'WHITE' else '♚'
    

# Movimientos de a una casilla en todas las direcciones

    def valid_positions(self, from_row, from_col, to_row, to_col):
        """Verifica si el movimiento del rey es válido."""
        directions = self._king_queen_directions_# Movimientos del rey (iguales que los de la reina pero limitados)
        possible_positions = self.get_possible_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions

    def get_possible_moves(self, from_row, from_col, directions):
        """Obtiene las posiciones válidas del rey desde una posición inicial."""
        return self.find_valid_moves(from_row, from_col, directions, single_step=True)  # Solo un paso
    