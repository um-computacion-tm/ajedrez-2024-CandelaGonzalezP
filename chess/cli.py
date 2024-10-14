from chess.chess import Chess
from chess.exceptions import *

def main():                                    
    chess = Chess()
    while chess.is_playing():
        play(chess)


def play(chess):
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
    print(chess.show_board())
    print("turn: ", chess.turn)


def get_input_coordinates(prompt, chess):
    row = input(f"{prompt} row ")
    if row.lower() == "stop":
        chess.tie()
        return None, None  # Retorna valores nulos para indicar que se detuvo el juego
    
    col = input(f"{prompt} col ")
    if col.lower() == "stop":
        chess.tie()
        return None, None  # Retorna valores nulos para indicar que se detuvo el juego
    return int(row), int(col)


def handle_move_error(exception):
    error_messages = {
        EmptyPosition: "No hay ninguna pieza en la posición de origen",
        OutOfBoard: "Movimiento fuera de tablero",
        DestinationInvalidMove: "Movimiento destino inválido",
        InvalidTurn: "No es tu turno",
        OriginInvalidMove: "Sin piezas en posición origen",
        InvalidMove: "Movimiento inválido"
    }
    print(error_messages[type(exception)])


"""
def play(chess):
    try:
        print(chess.show_board())
        print("turn: ", chess.turn)

        from_row = input("From row ")
        if from_row.lower()=="stop":
            return chess.tie() 
        
        from_col = input("From col ")
        if from_col.lower()=="stop":
            return chess.tie()
        
        to_row = input("To row ")
        if to_row.lower()=="stop":
            return chess.tie()
        
        to_col = input("To col ")
        if to_col.lower()=="stop":
            return chess.tie()
        
        from_row = int(from_row)
        from_col = int(from_col)
        to_row = int(to_row)
        to_col = int(to_col)

        chess.move(from_row, from_col, to_row, to_col)

    except EmptyPosition as e:
        print("No hay ninguna pieza en la posición de origen")
    except OutOfBoard as e:
        print("Movimiento fuera de tablero")
    except DestinationInvalidMove as e:
        print("Movimiento destino invalido")
    except InvalidTurn as e:
        print("No es tu turno")
    except OriginInvalidMove as e:
        print("Sin piezas en posicion origen")
    except InvalidMove as e:
        print("Movimiento inválido")
    except Exception as e:
        print("Error inesperado")  
"""
