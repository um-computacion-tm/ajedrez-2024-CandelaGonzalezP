from chess.pieces import Piece                 #ALFIL CLASE

class Bishop(Piece):

    def symbol(self):
        return 'B' if self.get_color() == "WHITE" else 'b'
    
# Movimientos en diagonal

    def is_valid_piece_move(self, from_row, from_col, to_row, to_col):
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        possible_positions = self.calculate_possible_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions














    def get_possible_positions(self, from_row, from_col):
        return self.possible_diagonal_positions(
            from_row,
            from_col,
        )
