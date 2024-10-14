class InvalidMove(Exception):

    """Excepción base para movimientos inválidos en el juego de ajedrez.

    Attributes:
        __message__ (str): Mensaje de error por defecto.
    """
    
    __message__ = "Movimieto de pieza invalido"
    def __str__(self):

        """Devuelve el mensaje de error.

        Returns:
            str: Mensaje de error que describe la excepción.
        """

        return self.__message__

class InvalidTurn(InvalidMove):

    """Excepción para indicar que no se puede mover una pieza del otro jugador.

    Inherits:
        InvalidMove: Excepción base para movimientos inválidos.

    Attributes:
        __message__ (str): Mensaje de error específico para el turno inválido.
    """

    __message__ = "No puedes mover pieza de otro jugador"

class EmptyPosition(InvalidMove):

    """Excepción para indicar que no se puede mover una pieza del otro jugador.

    Inherits:
        InvalidMove: Excepción base para movimientos inválidos.

    Attributes:
        __message__ (str): Mensaje de error específico para el turno inválido.
    """

    __message__ = "La posicion esta vacia"

class OutOfBoard(InvalidMove):

    """Excepción para indicar que una posición está fuera del tablero.

    Inherits:
        InvalidMove: Excepción base para movimientos inválidos.

    Attributes:
        __message__ (str): Mensaje de error específico para una posición fuera del tablero.
    """

    __message__ = "La posicion indicada se encuentra fuera del tablero"

class OriginInvalidMove(InvalidMove):

    """Excepción para indicar que un movimiento desde la posición de origen es inválido.

    Inherits:
        InvalidMove: Excepción base para movimientos inválidos.

    Attributes:
        __message__ (str): Mensaje de error específico para un movimiento inválido desde la posición de origen.
    """

    __message__ = "Movimiento inválido desde la posición de origen"

class DestinationInvalidMove(InvalidMove):

    """Excepción para indicar que un movimiento hacia la posición de destino es inválido.

    Inherits:
        InvalidMove: Excepción base para movimientos inválidos.

    Attributes:
        __message__ (str): Mensaje de error específico para un movimiento inválido hacia la posición de destino.
    """

    __message__ = "Movimiento inválido hacia la posición de destino"