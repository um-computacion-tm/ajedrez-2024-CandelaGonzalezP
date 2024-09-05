#excepciones: siempre se va de la mas particular a la mas general (engloba)
#def handle_value_error(e):                            # Funciones para manejar excepciones estándar
#    print(f"Error: {e}")
#    return False
#def handle_generic_exception(e):
#    print('error')

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