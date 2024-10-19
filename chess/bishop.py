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

    def valid_positions(self, from_row, from_col, to_row, to_col):
        available_moves = self.get_possible_moves(from_row, from_col)
        return (to_row, to_col) in available_moves

    def get_possible_moves(self, from_row, from_col):
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        return self.find_valid_moves(from_row, from_col, directions)
