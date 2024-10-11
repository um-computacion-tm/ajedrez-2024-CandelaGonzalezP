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
    



    def move(self, from_row, from_col, to_row, to_col):
        self.validate_move(from_row, from_col, to_row, to_col)
        self.__board__.move(from_row, from_col, to_row, to_col)
        
        if self.check_winner():
            print(f"El ganador es... : {self.__turn__}")
            return self.finish()
        
        self.change_turn()

    def validate_move(self, from_row, from_col, to_row, to_col):
        """Valida los parámetros del movimiento."""
        self.validate_coordinates(from_row, from_col, to_row, to_col)
        self.validate_piece(from_row, from_col)
        self.validate_turn(from_row, from_col)
        self.validate_move_validity(from_row, from_col, to_row, to_col)

    def validate_coordinates(self, from_row, from_col, to_row, to_col):
        """Valida que las coordenadas estén dentro de los límites."""
        if not (0 <= to_row < 8 and 0 <= to_col < 8):
            raise DestinationInvalidMove()

    def validate_piece(self, from_row, from_col):
        """Valida que haya una pieza en la posición inicial."""
        piece = self.__board__.get_piece(from_row, from_col)
        if not piece:
            raise EmptyPosition()

    def validate_turn(self, from_row, from_col):
        """Valida que sea el turno correcto para mover la pieza."""
        piece = self.__board__.get_piece(from_row, from_col)
        if piece.get_color() != self.__turn__:
            raise InvalidTurn()

    def validate_move_validity(self, from_row, from_col, to_row, to_col):
        """Valida que el movimiento de la pieza sea válido."""
        piece = self.__board__.get_piece(from_row, from_col)
        if not (piece.valid_move_1(from_row, from_col, to_row, to_col) or piece.valid_move_2(from_row, from_col, to_row, to_col)):
            raise InvalidMove()

    def check_winner(self):
        """Verifica si hay un ganador."""
        return self.ganador()



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