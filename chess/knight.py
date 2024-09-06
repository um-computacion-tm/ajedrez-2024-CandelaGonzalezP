from chess.pieces import Piece      #CABALLO CLASE

class Knight(Piece):
    
    def __str__(self):  
      if self.__color__ == "WHITE":
          return "♞"
      else:
         return "♘" 
      

#################### 
class Knight(Piece):
    def __init__(self, position, color, board):
        super().__init__(color, board)
        self.__position__ = position

    def get_possible_moves(self):
        x, y = self.__position__
        moves = []

        # Movimientos posibles del caballo
        possible_moves = [
            (x + 2, y + 1), (x + 2, y - 1),
            (x - 2, y + 1), (x - 2, y - 1),
            (x + 1, y + 2), (x + 1, y - 2),
            (x - 1, y + 2), (x - 1, y - 2),
        ]
        
        for move in possible_moves:
            if 0 <= move[0] < 8 and 0 <= move[1] < 8:  # Dentro del tablero
                piece = self.__board__.get_piece(move[0], move[1])
                # Solo agrega si la casilla está vacía o tiene una pieza del color opuesto
                if piece is None or piece.color != self.__color__:
                    moves.append(move)

        return moves
