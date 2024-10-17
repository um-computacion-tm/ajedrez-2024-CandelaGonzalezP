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
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        possible_positions = self.find_valid_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions
