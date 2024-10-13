from chess.pieces import Piece        #REY CLASE

class King(Piece):

    def symbol(self):
        return 'K' if self.get_color() == "WHITE" else 'k'

# Movimientos de a una casilla en todas las direcciones

    def king_valid_position(self, board, from_pos, to_pos):
        """Verificar si el movimiento es válido para el rey."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return max(abs(from_row - to_row), abs(from_col - to_col)) == 1


#no uso herencia