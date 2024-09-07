from chess.pieces import Piece                 #ALFIL CLASE

class Bishop(Piece):

    white_str = "♝"
    black_str = "♗"

    def get_possible_moves(self, board):              #calcula los movimientos posibles en las cuatro direcciones diagonales, verificando si la casilla está vacía o si contiene una pieza del oponente.
        moves = []
        x, y = self.__position__

        for i in range(1, 8):                                       # Movimiento diagonal (arriba a la derecha)
            new_x, new_y = x + i, y + i
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if board.get_piece(new_x, new_y) is None:
                    moves.append((new_x, new_y))
                elif board.get_piece(new_x, new_y).get_color() != self.get_color():
                    moves.append((new_x, new_y))
                    break
                else:
                    break

        for i in range(1, 8):                                       # Movimiento diagonal (arriba a la izquierda)
            new_x, new_y = x + i, y - i
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if board.get_piece(new_x, new_y) is None:
                    moves.append((new_x, new_y))
                elif board.get_piece(new_x, new_y).get_color() != self.get_color():
                    moves.append((new_x, new_y))
                    break
                else:
                    break

        for i in range(1, 8):                                      # Movimiento diagonal (abajo a la derecha)
            new_x, new_y = x - i, y + i
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if board.get_piece(new_x, new_y) is None:
                    moves.append((new_x, new_y))
                elif board.get_piece(new_x, new_y).get_color() != self.get_color():
                    moves.append((new_x, new_y))
                    break
                else:
                    break

        for i in range(1, 8):                                     # Movimiento diagonal (abajo a la izquierda)
            new_x, new_y = x - i, y - i
            if 0 <= new_x < 8 and 0 <= new_y < 8:
                if board.get_piece(new_x, new_y) is None:
                    moves.append((new_x, new_y))
                elif board.get_piece(new_x, new_y).get_color() != self.get_color():
                    moves.append((new_x, new_y))
                    break
                else:
                    break

        return moves

