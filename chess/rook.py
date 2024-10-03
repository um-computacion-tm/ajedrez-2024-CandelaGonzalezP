from chess.pieces import Piece       #TORRE CLASE

class Rook(Piece):

    def symbol(self):
        return 'R' if self.get_color() == "WHITE" else 'r'

# Movimientos ortogonales    

    def is_valid_piece_move(self, from_row, from_col, to_row, to_col):
        # Movimientos ortogonales: arriba, abajo, izquierda, derecha
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        possible_positions = self.calculate_possible_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions









    def valid_positions(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):

        possible_positions = (
            self.possible_positions_vd(from_row, from_col) +  # verticales hacia abajo
            self.possible_positions_va(from_row, from_col) +  # verticales hacia arriba
            self.possible_positions_hr(from_row, from_col) +  # horizontales hacia la derecha
            self.possible_positions_hl(from_row, from_col)    # horizontales hacia la izquierda
        )
        return (to_row, to_col) in possible_positions
