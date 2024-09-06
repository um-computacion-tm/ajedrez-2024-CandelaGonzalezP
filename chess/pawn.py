from chess.pieces import Piece      #PEON CLASE

class Pawn(Piece):

    def __str__(self):  
      if self.__color__ == "WHITE":
          return "♟"
      else:
         return "♙" 