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

    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_positions = self.get_possible_moves(from_row, from_col)
        return (to_row, to_col) in possible_positions

    def get_possible_moves(self, from_row, from_col):
        knight_moves = [
            (from_row + 2, from_col + 1), (from_row + 2, from_col - 1),
            (from_row - 2, from_col + 1), (from_row - 2, from_col - 1),
            (from_row + 1, from_col + 2), (from_row + 1, from_col - 2),
            (from_row - 1, from_col + 2), (from_row - 1, from_col - 2)
        ]
        return knight_moves

"""
    def knight_valid_position(self, board, from_pos, to_pos):
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return (abs(from_row - to_row) == 2 and abs(from_col - to_col) == 1) or \
               (abs(from_row - to_row) == 1 and abs(from_col - to_col) == 2)
"""