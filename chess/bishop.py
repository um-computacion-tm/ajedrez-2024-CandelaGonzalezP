from chess.pieces import Piece                 #ALFIL CLASE

class Bishop(Piece):

    def symbol(self):
        return 'B' if self.get_color() == "WHITE" else 'b'

    def get_possible_positions(self, from_row, from_col):
        return self.possible_diagonal_positions(
            from_row,
            from_col,
        )


 #agregar movimientos diagonales (hecho)