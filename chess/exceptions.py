#excepciones: siempre se va de la mas particular a la mas general (engloba)

class InvalidMove(Exception):
    message = "Movimieto de pieza invalido"
    def __str__(self):
        return self.message

class InvalidTurn(InvalidMove):
    message = "No puedes mover pieza de otro jugador"

class EmptyPosition(InvalidMove):
    message = "La posicion esta vacia"

class OutOfBoard(InvalidMove):
    message = "La posicion indicada se encuentra fuera del tablero"

class OriginInvalidMove(InvalidMove):
    message = "Movimiento inválido desde la posición de origen"

class DestinationInvalidMove(InvalidMove):
    message = "Movimiento inválido hacia la posición de destino"