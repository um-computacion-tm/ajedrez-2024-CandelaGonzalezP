from chess.pieces import Piece        #REY CLASE

class King(Piece):

    def __str__(self):  
      if self.__color__ == "WHITE":
          return "♚"
      else:
         return "♔" 