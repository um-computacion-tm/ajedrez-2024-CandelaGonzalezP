from chess.board import Board
from chess.exceptions import *

class Chess:

    def __init__(self):

        """
        Inicializa el juego de ajedrez.

        Crea una instancia del tablero y establece el turno inicial
        en "WHITE" (blancas).
        """

        self.__board__ = Board()
        self.__turn__ = "WHITE"  # El turno comienza con el jugador de blancas
        
    def switch_turn(self):

        """
        Cambia el turno del jugador actual.

        Alterna el turno entre "WHITE" y "BLACK".
        
        No recibe parámetros y no devuelve ningún valor.
        """

        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"

    def get_turn(self):

        """
        Obtiene el turno actual del juego.

        Returns:
            str: El color del jugador cuyo turno es ("WHITE" o "BLACK").
        """

        return self.__turn__
    
    def is_game_over(self):

        """
        Verifica si el juego ha terminado.

        El juego se considera terminado si un jugador no tiene más
        piezas en el tablero.

        Returns:
            bool: True si el juego ha terminado, False de lo contrario.
        """

        if self.__board__.count_pieces("WHITE") == 0 or self.__board__.count_pieces("BLACK") == 0:
            return True
        return False

    def make_move(self, from_row, from_col, to_row, to_col):

        """
        Realiza un movimiento en el tablero.

        Valida el movimiento de una pieza desde la posición de origen
        hasta la posición de destino y actualiza el estado del juego.
        
        Args:
            from_row (int): Fila de la posición de origen.
            from_col (int): Columna de la posición de origen.
            to_row (int): Fila de la posición de destino.
            to_col (int): Columna de la posición de destino.

        Raises:
            EmptyPosition: Si no hay pieza en la posición de origen.
            InvalidTurn: Si se intenta mover una pieza que no pertenece al jugador actual.
            DestinationInvalidMove: Si el movimiento no es válido para la pieza.

        No devuelve ningún valor.
        """

        piece = self.__board__.get_piece(from_row, from_col)
        if piece is None:
            raise EmptyPosition()
        if piece.get_color() != self.__turn__:
            raise InvalidTurn()
        if not piece.valid_positions(from_row, from_col, to_row, to_col):
            raise DestinationInvalidMove()
        self.__board__.move(from_row, from_col, to_row, to_col)
        self.switch_turn()