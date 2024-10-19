from chess.pieces import Piece       #TORRE

class Rook(Piece):

    """
    Clase que representa una torre en el juego de ajedrez.

    Hereda de la clase Piece, lo que proporciona las funcionalidades básicas 
    para las piezas del juego.
    """

    def symbol(self):
        return '♖' if self.get_color() == 'WHITE' else '♜'


# Movimientos ortogonales

    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_positions = self.get_possible_moves(from_row, from_col)
        position_to_check = (to_row, to_col)
        return position_to_check in possible_positions

    def get_possible_moves(self, from_row, from_col):
        directions = self.get_rook_directions()
        return self.find_valid_moves(from_row, from_col, directions)

    def get_rook_directions(self):
        return [(1, 0), (-1, 0), (0, -1), (0, 1)]
