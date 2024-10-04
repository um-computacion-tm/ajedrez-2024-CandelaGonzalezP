from chess.board import Board
from chess.exceptions import *
import sys
    
class Chess:                      

# inicializa 

    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

# Verificar que el juego esta en curso

    def is_playing(self):        #identifica si el juego esta en curso
        return True
    
# Realizar movimientos en el tablero

    def move (
        self,
        from_row,
        from_col,
        to_row,
        to_col,
    ):
        
#validate coords
        piece = self.__board__.get_piece(from_row, from_col)
        if not piece:
            raise EmptyPosition()
        if not (0<=to_row<8 and 0<=to_col<8):
            raise DestinationInvalidMove()
        if not piece.get_color() == self.__turn__: 
            raise InvalidTurn()
        if not piece.valid_move_1(from_row, from_col, to_row, to_col) and not piece.valid_move_2(from_row, from_col, to_row, to_col):
            raise InvalidMove()
        self.__board__.move(from_row, from_col, to_row, to_col)
        if self.ganador():
          print(f"El ganador es... : {self.turn}")
          return self.finish()
        self.change_turn()

# Usuario elige terminan o no la partida (ofrece empate)

    def offer_draw(self):
        import sys
        print("¿Quiere terminar la partida? (si/no)")
        user_input = input().strip().lower()
        if user_input == "si":
            print("Su partida ha sido terminada, gracias por jugar!")
            return self.finish()
        else:
            print("Su partida continúa.")
            return True


# Verifica equipo ganador del ajedrez

    def ganador(self):
        opponent_color="Black" if self.__turn__=="White" else "White"
        return self.__board__.count_pieces(opponent_color)==0

# propertys

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

    def finish(self):
        return sys.exit()      #sys: maneja la entrada/salida estándar