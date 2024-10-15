from chess.board import Board
from chess.exceptions import *
import sys
    
class Chess:                      

    """Clase que representa un juego de ajedrez."""

    def __init__(self):

        """Inicializa una nueva instancia de Chess.

        Crea un nuevo tablero y establece el turno inicial en blanco.
        """

        self.__board__ = Board()
        self.__turn__ = "WHITE"

    def is_playing(self):

        """Verifica si el juego está en curso.

        Returns:
            bool: Siempre devuelve True, indicando que el juego está en curso.
        """

        return True
    
# Realizar movimientos en el tablero

    def move(self, from_row, from_col, to_row, to_col):

        """Realiza un movimiento de una pieza en el tablero.

        Args:
            from_row (int): Fila de la posición de origen.
            from_col (int): Columna de la posición de origen.
            to_row (int): Fila de la posición de destino.
            to_col (int): Columna de la posición de destino.

        Raises:
            EmptyPosition: Si la posición de origen está vacía.
            DestinationInvalidMove: Si la posición de destino está fuera del tablero.
            InvalidTurn: Si no es el turno del jugador correspondiente.
            InvalidMove: Si el movimiento de la pieza no es válido.

        Returns:
            None: Imprime el ganador si el movimiento resulta en un jaque mate y termina el juego.
        """

        piece = self.__board__.get_piece(from_row, from_col)        
        move = {'from_row': from_row, 'from_col': from_col, 'to_row': to_row, 'to_col': to_col}
        self.validate_move(piece, move)
        self.__board__.move(from_row, from_col, to_row, to_col)
        if self.ganador():
            print(f"El ganador es... : {self.turn}")
            return self.finish()
        self.change_turn()


    def validate_move(self, piece, move):
        """Valida que el movimiento de la pieza sea válido."""
        
        from_row, from_col, to_row, to_col = move['from_row'], move['from_col'], move['to_row'], move['to_col']
        self.check_empty_position(piece)  # Verificar si hay una pieza en la posición
        self.check_within_board(to_row, to_col)  # Verificar si el movimiento está dentro del tablero

        # Debug: Imprimir el color de la pieza y el turno actual
        print(f"Color de la pieza: {piece.get_color() if piece else 'None'}, Turno actual: {self.__turn__}")

        self.check_turn(piece)  # Verificar que sea el turno correcto
        from_position = {'from_row': from_row, 'from_col': from_col}  # Crear un diccionario
        self.check_valid_move(piece, from_position, to_row, to_col) 


    def check_empty_position(self, piece):

        """Verifica si hay una pieza en la posición de origen.

        Args:
            piece (Piece): La pieza a verificar.

        Raises:
            EmptyPosition: Si no hay pieza en la posición de origen.

        Returns:
            None: No devuelve nada.
        """

        if not piece:
            raise EmptyPosition()

    def check_within_board(self, to_row, to_col):

        """Verifica que la posición de destino esté dentro del tablero.

        Args:
            to_row (int): Fila de la posición de destino.
            to_col (int): Columna de la posición de destino.

        Raises:
            DestinationInvalidMove: Si la posición de destino está fuera del tablero.

        Returns:
            None: No devuelve nada.
        """

        if not (0 <= to_row < 8 and 0 <= to_col < 8):
            raise DestinationInvalidMove()

    def check_turn(self, piece):
        """Verifica que sea el turno correcto del jugador."""
        
        if piece is None:
            raise EmptyPosition()  # Asegúrate de que la pieza existe
        if piece.get_color() != self.__turn__:
            raise InvalidTurn() 


    def check_valid_move(self, piece, from_position, to_row, to_col):

        """Verifica que el movimiento de la pieza sea válido.

        Args:
            piece (Piece): La pieza a mover.
            from_position (dict): Diccionario que contiene las posiciones de origen.
            to_row (int): Fila de la posición de destino.
            to_col (int): Columna de la posición de destino.

        Raises:
            InvalidMove: Si el movimiento de la pieza no es válido.

        Returns:
            None: No devuelve nada.
        """

        from_row, from_col = from_position['row'], from_position['col']
        if not piece.valid_move_1(from_row, from_col, to_row, to_col) and not piece.valid_move_2(from_row, from_col, to_row, to_col):
            raise InvalidMove()

        
# Usuario elige terminan o no la partida (ofrece empate)

    def offer_draw(self):

        """Pregunta al usuario si desea terminar la partida ofreciendo un empate.

        Returns:
            None: Si el usuario acepta, termina la partida. Si no, continúa el juego.
        """

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

        """Verifica si hay un ganador en el juego.

        Returns:
            bool: Devuelve True si el oponente no tiene piezas restantes; de lo contrario, False.
        """

        opponent_color="BLACK" if self.__turn__=="WHITE" else "WHITE"
        return self.__board__.count_pieces(opponent_color)==0

# propertys

    @property                 
    def turn(self):
        return self.__turn__



    def show_board(self):    

        """Devuelve una representación en cadena del tablero.

        Returns:
            str: Representación en cadena del tablero.
        """

        return str(self.__board__)


    def change_turn(self):     
        """Alterna el turno entre 'WHITE' y 'BLACK'.

        Returns:
            None: No devuelve nada.
        """
        if self.__turn__ == 'WHITE':
            self.__turn__ = 'BLACK'
        else:
            self.__turn__ = 'WHITE'


    def finish(self):

        """Termina la partida y cierra el programa.

        Returns:
            None: Termina la ejecución del programa.
        """

        return sys.exit()      
    


# agregado change turn cambiso chats
