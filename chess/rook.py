from chess.pieces import Piece       #TORRE CLASE

class Rook(Piece):

    white_str = "♜"
    black_str = "♖"

    def valid_positions(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        possible_positions = (
            self.possible_positions_vd(from_row, from_col) +
            self.possible_positions_va(from_row, from_col)
        )
        return (to_row, to_col) in possible_positions

    def possible_positions_vd(self, row, col):
        possibles = []
        for next_row in range(row + 1, 8):
            # que la celda que sigue no este ocupada..
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles

    def possible_positions_va(self, row, col):
        possibles = []
        for next_row in range(row - 1, -1, -1):
            possibles.append((next_row, col))
        return possibles

#    def get_possible_moves(self, board):          #Define movimientos posibles en el tablero
#        moves = []
#        x, y = self.__position__
#
#        for i in range(8):                                   # MOVIMIENTO HORIZONTAL
#            if i != x:                                       # No incluir la posición actual
#                if board.get_piece(i, y) is None:
#                    moves.append((i, y))
#                elif board.get_piece(i, y).__color__ != self.__color__:
#                    moves.append((i, y))
#                    break                                     # Detenerse si encuentra una pieza del color contrario
#                else:
#                    break                                     # Detenerse si encuentra una pieza del mismo color
#
#        for j in range(8):                                    # MOVIMIENTO VERTICAL
#            if j != y:                                        # No incluir la posición actual
#                if board.get_piece(x, j) is None:
#                    moves.append((x, j))
#                elif board.get_piece(x, j).__color__ != self.__color__:
#                    moves.append((x, j))
#                    break
#                else:
#                    break
#        
#        return moves