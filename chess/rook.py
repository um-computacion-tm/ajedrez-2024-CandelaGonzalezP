from chess.pieces import Piece       #TORRE CLASE

class Rook(Piece):

    def symbol(self):
        return 'R' if self.get_color() == "WHITE" else 'r'


    def rook_valid_positions(self, from_row, from_col, to_row, to_col):
        # Movimientos ortogonales: arriba, abajo, izquierda, derecha
        directions = self.get_rook_directions()
        possible_positions = self.find_valid_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions

    def get_rook_directions(self):
        # Movimientos ortogonales: arriba, abajo, izquierda, derecha
        return [(1, 0), (-1, 0), (0, -1), (0, 1)]


#uso herencia