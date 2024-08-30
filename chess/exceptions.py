#excepciones: siempre se va de la mas particular a la mas general (engloba)

class InvalidMoveNoPiece(InvalidMove):                #Excepción para un movimiento desde una casilla vacía.
    ...

class InvalidMoveRookMove(InvalidMove):               #Excepción para un movimiento inválido de la torre.
    ...

class InvalidMove(Exception):                         # Clase base para excepciones de movimientos inválidos
    ...

#def handle_value_error(e):                            # Funciones para manejar excepciones estándar
#    print(f"Error: {e}")
#    return False

#def handle_generic_exception(e):
#    print('error')