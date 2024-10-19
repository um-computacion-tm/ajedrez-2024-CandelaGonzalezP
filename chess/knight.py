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
        potential_moves = self.get_possible_moves(from_row, from_col)
        check_position = (to_row, to_col)
        return check_position in potential_moves

    def get_possible_moves(self, from_row, from_col):
        knight_moves = [
            (from_row + 2, from_col + 1), (from_row + 2, from_col - 1),
            (from_row - 2, from_col + 1), (from_row - 2, from_col - 1),
            (from_row + 1, from_col + 2), (from_row + 1, from_col - 2),
            (from_row - 1, from_col + 2), (from_row - 1, from_col - 2)
        ]
        return knight_moves
