from chess.chess import Chess
from chess.exceptions import *

def main():    

    """Función principal que inicia el juego de ajedrez.

    Crea una instancia de Chess y gestiona el bucle principal del juego.
    """

    chess = Chess()
    while chess.is_playing():
        play(chess)


def play(chess):

    """Gestiona un turno de juego en el ajedrez.

    Muestra el tablero, obtiene las coordenadas de movimiento del jugador,
    y realiza el movimiento en el tablero.

    Args:
        chess (Chess): La instancia del juego de ajedrez.

    Raises:
        EmptyPosition: Si la posición de origen está vacía.
        OutOfBoard: Si el movimiento está fuera del tablero.
        DestinationInvalidMove: Si la posición de destino es inválida.
        InvalidTurn: Si no es el turno del jugador correspondiente.
        OriginInvalidMove: Si no hay piezas en la posición de origen.
        InvalidMove: Si el movimiento de la pieza no es válido.

    Returns:
        None: No devuelve nada.
    """

    try:
        display_board(chess)
        from_row, from_col = get_input_coordinates("From", chess)
        to_row, to_col = get_input_coordinates("To", chess)
        chess.move(from_row, from_col, to_row, to_col)
    except (EmptyPosition, OutOfBoard, DestinationInvalidMove, InvalidTurn, OriginInvalidMove, InvalidMove) as e:
        handle_move_error(e)
    except Exception as e:
        print("Error inesperado")


def display_board(chess):

    """Muestra el estado actual del tablero de ajedrez.

    Args:
        chess (Chess): La instancia del juego de ajedrez.

    Returns:
        None: No devuelve nada, solo imprime el tablero y el turno actual.
    """

    print(chess.show_board())
    print("turn: ", chess.turn)


def get_input_coordinates(prompt, chess):

    """Obtiene las coordenadas de entrada del usuario para el movimiento.

    Args:
        prompt (str): Mensaje para indicar al usuario que ingrese coordenadas.
        chess (Chess): La instancia del juego de ajedrez.

    Returns:
        tuple: Devuelve una tupla con las coordenadas (fila, columna) como enteros.
               Retorna (None, None) si el usuario elige detener el juego.
    """

    row = input(f"{prompt} row ")
    if row.lower() == "stop":
        chess.tie()
        return None, None  
    col = input(f"{prompt} col ")
    if col.lower() == "stop":
        chess.tie()
        return None, None  
    return int(row), int(col)


def handle_move_error(exception):

    """Maneja los errores de movimiento y muestra el mensaje correspondiente.

    Args:
        exception (Exception): La excepción que se produjo.

    Returns:
        None: No devuelve nada, solo imprime el mensaje de error correspondiente.
    """

    error_messages = {
        EmptyPosition: "No hay ninguna pieza en la posición de origen",
        OutOfBoard: "Movimiento fuera de tablero",
        DestinationInvalidMove: "Movimiento destino inválido",
        InvalidTurn: "No es tu turno",
        OriginInvalidMove: "Sin piezas en posición origen",
        InvalidMove: "Movimiento inválido"
    }
    print(error_messages[type(exception)])