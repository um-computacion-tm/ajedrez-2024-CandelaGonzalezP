class Piece:                       #HERENCIA PIEZAS 

    def __init__(self, color, board):
        self.__color__ = color
        self.__board__ = board

    def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_str
        else:
            return self.black_str
        
    def get_color(self):
        return self.__color__