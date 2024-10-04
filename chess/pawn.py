from chess.pieces import Piece      #PEON CLASE

class Pawn(Piece):

    def symbol(self):
        return 'P' if self.get_color() == "WHITE" else 'p'

# Movimientos hacia adelante y captura

    def is_valid_piece_move(self, from_row, from_col, to_row, to_col):
        forward_moves = [(1, 0)] if self.__color__ == "BLACK" else [(-1, 0)]       # Direcciones para avanzar del peón
        if (self.__color__ == "BLACK" and from_row == 1) or (self.__color__ == "WHITE" and from_row == 6):        # Si el peón está en su posición inicial, puede avanzar dos casillas
            forward_moves.append((2, 0) if self.__color__ == "BLACK" else (-2, 0))

# Posiciones posibles para avanzar
        valid_positions = []
        for move in forward_moves:
            next_row = from_row + move[0]
            next_col = from_col + move[1]
            if 0 <= next_row < 8 and 0 <= next_col < 8:
                if self.__board__.get_piece(next_row, next_col) is None:
                    valid_positions.append((next_row, next_col))
                else:
                    break  # Detenerse si hay una pieza en el camino

# Direcciones para capturas en diagonal
        diagonal_captures = [(1, 1), (1, -1)] if self.__color__ == "BLACK" else [(-1, 1), (-1, -1)]
        
        for capture in diagonal_captures:
            next_row, next_col = from_row + capture[0], from_col + capture[1]
            if 0 <= next_row < 8 and 0 <= next_col < 8:
                opponent_piece = self.__board__.get_piece(next_row, next_col)
                if opponent_piece and opponent_piece.get_color() != self.__color__:
                    valid_positions.append((next_row, next_col))  # Solo se puede capturar si hay una pieza enemiga

        return (to_row, to_col) in valid_positions