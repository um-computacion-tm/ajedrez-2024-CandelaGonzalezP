from chess.pieces import Piece         #REINA CLASE

class Queen(Piece):
    
    def symbol(self):
        return 'Q' if self.get_color() == "WHITE" else 'q'
    
    def get_possible_positions(self, from_row, from_col):
        return self.possible_diagonal_positions(
            from_row,
            from_col,
        )
    
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


#tengo movimientos ortogonales (hecho)
#agregar movimientos diagonales (hecho)
