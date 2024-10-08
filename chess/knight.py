from chess.pieces import Piece      #CABALLO CLASE

class Knight(Piece):
        
    def symbol(self):
        return 'N' if self.get_color() == "WHITE" else 'n'    

# Movimientos en L en toda direccion

    def is_valid_piece_move(self, board, from_pos, to_pos):
        """Verificar si el movimiento es válido para el caballo."""
        """El caballo se mueve en forma de "L". """
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        return (abs(from_row - to_row) == 2 and abs(from_col - to_col) == 1) or \
               (abs(from_row - to_row) == 1 and abs(from_col - to_col) == 2)
