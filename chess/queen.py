from chess.pieces import Piece         #REINA CLASE

class Queen(Piece):
    
    def symbol(self):
        return 'Q' if self.get_color() == "WHITE" else 'q'

    def queen_valid_positions(self, move, directions=None):
        """Verifica si el movimiento del rey es válido."""
        from_row, from_col, to_row, to_col = move['from_row'], move['from_col'], move['to_row'], move['to_col']
        if directions is None:
            directions = self.__king_queen_directions__
        
        possible_positions = self.find_valid_moves(from_row, from_col, directions, single_step=False)
        return (to_row, to_col) in possible_positions


#uso herencia
