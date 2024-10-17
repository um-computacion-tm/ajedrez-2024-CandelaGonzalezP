from chess.pieces import Piece         #REINA

class Queen(Piece):
    
    """
    Clase que representa una reina en el juego de ajedrez.
    
    Hereda de la clase Piece, lo que proporciona las funcionalidades básicas 
    para las piezas del juego.
    """

    def symbol(self):
        return '♕' if self.get_color() == 'WHITE' else '♛'

# Movimientos en diagonal y ortogonales

    def queen_valid_positions(self, move, directions=None):
        from_row, from_col, to_row, to_col = move['from_row'], move['from_col'], move['to_row'], move['to_col']
        if directions is None:
            directions = self.__king_queen_directions__
        possible_positions = self.find_valid_moves(from_row, from_col, directions, single_step=False)
        return (to_row, to_col) in possible_positions
