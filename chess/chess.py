from chess.board import Board

class Chess:                      #inicializa un nuevo juego de ajedrez creando un tablero con la clase Board y establece el turno inicial en "WHITE"

    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def is_playing(self):        #identifica si el juego esta en curso
        return True
    
    # Obtiene la pieza en la posición de origen: Busca y guarda la pieza ubicada en la posición (from_row, from_col) del tablero. Cambia el turno
    def move (
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        piece = self.__board__.get_piece(from_row, from_col)
        self.change_turn()

    @property                 #Retorna el color del jugador cuyo turno es el actual.
    def turn(self):
        return self.__turn__

    def show_board(self):             #Devuelve una representación en cadena del tablero.
        return str(self.__board__)

    def change_turn(self):            #Alterna el turno entre "white" y "black".
        if self.__turn__ == 'white':
            self.__turn__ = 'black'
        else:
            self.__turn__ = 'white'