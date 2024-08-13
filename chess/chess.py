class Chess:

    def __init__():
        self.__board__ = Board ()
        self.__turn__ = 'white'


    def move (
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        piece = self.board.get_piece(from_row, from_col)   #no tiene __porque get piece es publico
        self.change_turn()

    def change_turn(self):
        if self.__turn__ == 'white':
            self.__turn__ = 'black'
        else:
            self.__turn__ = 'white'