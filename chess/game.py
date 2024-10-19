from chess.board import Board
from chess.exceptions import *

class Chess:

    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"  # El turno comienza con el jugador de blancas
        
    def switch_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"

    def get_turn(self):
        return self.__turn__
    
    def is_game_over(self):
        if self.__board__.count_pieces("WHITE") == 0 or self.__board__.count_pieces("BLACK") == 0:
            return True
        return False

    def make_move(self, from_row, from_col, to_row, to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if piece is None:
            raise EmptyPosition()
        if piece.get_color() != self.__turn__:
            raise InvalidTurn()
        if not piece.valid_positions(from_row, from_col, to_row, to_col):
            raise DestinationInvalidMove()
        self.__board__.move(from_row, from_col, to_row, to_col)

        self.switch_turn()