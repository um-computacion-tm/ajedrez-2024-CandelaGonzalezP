from chess.pieces import Piece        #REY CLASE

class King(Piece):

    white_str ="♚"
    black_str = "♔" 

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


    def get_possible_positions(self, from_row, from_col):
        possibles = self.possible_orthogonal_positions(
            from_row,
            from_col,
        ) + self.possible_diagonal_positions(
            from_row,
            from_col,
        )
        possible_king = []
        for (possible_row, possible_col) in possibles:
            if (
                abs(from_row - possible_row) <= 1 and
                abs(from_col - possible_col) <= 1
            ):
                possible_king.append((possible_row, possible_col))
        return possible_king





#agregar movientos ortogonales y diagonales
#distancia mov ort
#agregar distancia para las diagonales
