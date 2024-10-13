from chess.pieces import Piece                 #ALFIL CLASE

class Bishop(Piece):

    def symbol(self):
        return 'B' if self.get_color() == "WHITE" else 'b'
    
# Movimientos en diagonal

    def bishop_valid_position(self, from_row, from_col, to_row, to_col):
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        possible_positions = self.find_valid_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions
    
#uso de herencia