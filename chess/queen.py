from chess.pieces import Piece         #REINA CLASE

class Queen(Piece):

    def __str__(self):  
      if self.__color__ == "WHITE":
          return "♛"
      else:
         return "♕"  