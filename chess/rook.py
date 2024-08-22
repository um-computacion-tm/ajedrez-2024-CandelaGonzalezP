from chess.pieces import Piece       #TORRE CLASE

class Rook (Piece):

    def __init__(self, position, color):
        super().__init__(color)
        self.__position__ = position

    def __str__(self):
        if self.__color__ == "WHITE":
            return "♜"
        else:
            return "♖"
        
    def get_possible_moves(self, board):
        moves = []
        x, y = self.__position__

        for i in range(8):                                   # MOVIMIENTO HORIZONTAL
            if i != x:                                       # No incluir la posición actual
                if board.get_piece(i, y) is None:
                    moves.append((i, y))
                elif board.get_piece(i, y).__color__ != self.__color__:
                    moves.append((i, y))
                    break                                     # Detenerse si encuentra una pieza del color contrario
                else:
                    break                                     # Detenerse si encuentra una pieza del mismo color

        for j in range(8):                                    # MOVIMIENTO VERTICAL
            if j != y:                                        # No incluir la posición actual
                if board.get_piece(x, j) is None:
                    moves.append((x, j))
                elif board.get_piece(x, j).__color__ != self.__color__:
                    moves.append((x, j))
                    break
                else:
                    break
        
        return moves