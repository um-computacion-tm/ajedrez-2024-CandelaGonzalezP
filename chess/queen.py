from chess.pieces import Piece         #REINA CLASE

class Queen(Piece):
    
    def symbol(self):
        return 'Q' if self.get_color() == "WHITE" else 'q'


    def queen_valid_positions(self, from_row, from_col, to_row, to_col, directions=None):
        if directions is None:
            directions = self.__king_queen_directions__
        possible_positions = self.find_valid_moves(from_row, from_col, directions, single_step=False)
        return (to_row, to_col) in possible_positions


#uso herencia

"""
# Movimientos ortogonales y diagonales
    def calculate_possible_moves(self, current_row, current_col, restrict_to_single_step=False):
        movement_directions = [
            (1, 0),   # Abajo
            (-1, 0),  # Arriba
            (0, 1),   # Derecha
            (0, -1),  # Izquierda
            (1, 1),   # Diagonal Abajo Derecha
            (1, -1),  # Diagonal Abajo Izquierda
            (-1, 1),  # Diagonal Arriba Derecha
            (-1, -1)  # Diagonal Arriba Izquierda
        ]
        
        return self._calculate_moves_in_directions(current_row, current_col, movement_directions, restrict_to_single_step)

    def _calculate_moves_in_directions(self, current_row, current_col, directions, restrict_to_single_step):
        valid_moves = []

        for delta_row, delta_col in directions:
            next_row, next_col = current_row + delta_row, current_col + delta_col
            
            while 0 <= next_row < 8 and 0 <= next_col < 8:
                target_piece = self.__board__.get_piece(next_row, next_col)

                if target_piece is not None:
                    if target_piece.get_color() != self.get_color():
                        valid_moves.append((next_row, next_col))  # Puede capturar
                    break  # Detenerse si hay una pieza en la posición

                valid_moves.append((next_row, next_col))  # Agregar movimiento válido

                if restrict_to_single_step:
                    break

                next_row += delta_row
                next_col += delta_col

        return valid_moves
"""
