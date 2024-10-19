from chess.pieces import Piece

class Queen(Piece):
    
    """
    Clase que representa una reina en el juego de ajedrez.
    
    Hereda de la clase Piece, lo que proporciona las funcionalidades básicas 
    para las piezas del juego.
    """

    def symbol(self):
        return '♕' if self.get_color() == 'WHITE' else '♛'

# Movimientos en diagonal y ortogonales

    def valid_positions(self, from_row, from_col, to_row, to_col):
        directions = self._king_queen_directions_  # Movimientos ortogonales y diagonales
        possible_positions = self.get_possible_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions

    def get_possible_moves(self, from_row, from_col, directions):
        return self.find_valid_moves(from_row, from_col, directions, single_step=False)
    