from chess.pieces import Piece      #PEON CLASE

class Pawn(Piece):

    def symbol(self):
        return 'P' if self.get_color() == "WHITE" else 'p'


    def pawns_valid_positions(self, from_row, from_col, to_row, to_col):
        valid_positions = []
        valid_positions.extend(self.get_forward_moves(from_row, from_col))
        valid_positions.extend(self.get_diagonal_captures(from_row, from_col))
        
        return (to_row, to_col) in valid_positions


    def get_forward_moves(self, from_row, from_col):
        forward_moves = self.get_initial_forward_moves(from_row)
        valid_positions = []

        for move in forward_moves:
            next_row, next_col = from_row + move[0], from_col + move[1]
            if self.is_valid_move(next_row, next_col):
                valid_positions.append((next_row, next_col))
            else:
                break  # Detenerse si hay una pieza en el camino

        return valid_positions

    def get_initial_forward_moves(self, from_row):
        # Direcciones para avanzar del peón
        forward_moves = [(1, 0)] if self.__color__ == "BLACK" else [(-1, 0)]
        
        # Si el peón está en su posición inicial, puede avanzar dos casillas
        if self.is_initial_position(from_row):
            forward_moves.append(self.get_double_step_move())
        
        return forward_moves

    def is_initial_position(self, from_row):
        return (self.__color__ == "BLACK" and from_row == 1) or (self.__color__ == "WHITE" and from_row == 6)

    def get_double_step_move(self):
        return (2, 0) if self.__color__ == "BLACK" else (-2, 0)

    def is_valid_move(self, row, col):
        return (0 <= row < 8 and 0 <= col < 8) and (self.__board__.get_piece(row, col) is None)


    def get_diagonal_captures(self, from_row, from_col):
        diagonal_captures = [(1, 1), (1, -1)] if self.__color__ == "BLACK" else [(-1, 1), (-1, -1)]
        valid_positions = []
        
        for capture in diagonal_captures:
            next_row, next_col = from_row + capture[0], from_col + capture[1]
            if self.is_valid_capture(next_row, next_col):
                valid_positions.append((next_row, next_col))  # Solo se puede capturar si hay una pieza enemiga
        
        return valid_positions


    def is_valid_capture(self, row, col):
        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        opponent_piece = self.__board__.get_piece(row, col)
        return opponent_piece and opponent_piece.get_color() != self.__color__


#no uso herencia