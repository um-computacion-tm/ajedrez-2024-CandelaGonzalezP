from chess.pieces import Piece         #REINA CLASE

class Queen(Piece):
    
    white_str = "♛"
    black_str = "♕"
    

    def get_possible_positions(self, from_row, from_col):
        return self.possible_orthogonal_positions(
            from_row,
            from_col,
        ) + self.possible_diagonal_positions(
            from_row,
            from_col,
        )
    


#tengo movimientos ortogonales
#agregar movimientos diagonales
