from chess.board import Board
from chess.exceptions import *

class Chess:

    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"  #inician las blancas


    def is_playing(self):
        return True

    def move(
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        piece = self.__board__.get_piece(from_row, from_col)
        if not piece:
            raise EmptyPosition() 
        if not piece.get_color == self.__turn__:  
            raise InvalidTurn()
        if self.__board__.get_piece(to_row, to_col) and self.__board__.get_piece(to_row, to_col).get_color == self.__turn__:
            raise SelfCaptureException()  
        if not piece.valid_positions(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        self.__board__.move(from_row, from_col, to_row, to_col)
        self.change_turn()


    def ganador(self):

        opponent_color = "BLACK" if self.turn == "WHITE" else "WHITE"
        if self.__board__.count_pieces(opponent_color) == 0:
            winner = "WHITE" if opponent_color == "BLACK" else "BLACK"
            print(f" CONGRATULATION!, {winner} WINS")
            return True
        return False
    

    def offer_draw(self):
        """Maneja la oferta de empate y verifica si ambos jugadores acuerdan."""
        if not self._offer_draw_:
            self._offer_draw_ = True
            print(f"{self._turn_} ha ofrecido un empate.")
            return "OFFER_MADE"
        else:
            self._offer_draw_ = False
            return "DRAW_ACCEPTED"

    def reject_draw(self):
        """Rechaza la oferta de empate actual."""
        self._offer_draw_ = False
        print("El jugador ha rechazado el empate.")
        

    @property
    def turn(self):
        return self.__turn__
    
    def show_board(self):
        return str(self.__board__)

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"

    def get_board(self):
        return self.__board__