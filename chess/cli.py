from chess.chess import Chess
from chess.exceptions import *
import sys

def main():                                    
    chess = Chess()
    while chess.is_playing():
        play(chess)


def play (chess):

    try:
        print(chess.show_board()) 
        print("turn: ", chess.turn)
        print("Ingrese su movimiento o EXIT para terminar: ")
        from_row = input("Desde fila: ").strip().upper()
        if from_row == "EXIT":
            print("El jugador ha terminado la partida.")
            exit()
        from_col = input("Desde columna: ").strip().upper()
        if from_col == "EXIT":                      
            print("El jugador ha terminado la partida.")
            exit()
        to_row = input("Hacia fila: ").strip().upper()
        if to_row == "EXIT":
            print("El jugador ha terminado la partida.")
            exit()
        to_col = input("Hacia columna: ").strip().upper()
        if to_col == "EXIT":
            print("El jugador ha terminado la partida.")
            exit()
        try:
            from_row = int(from_row)
            from_col = int(from_col)
            to_row = int(to_row)
            to_col = int(to_col)
        except ValueError:
            raise InvalidCoordinateInputError

        chess.move(
            from_row,
            from_col,
            to_row,
            to_col
        )

        # Verificar si hay un ganador
        ganador = chess.ganador()
        if ganador:
            print(print(f"El juego ha terminado. {ganador} es el ganador."))  # Imprimir el mensaje de quién ganó
            sys.exit()  # Salir del programa
        return

#las excepciones se ponen de la mas particular a la mas general
    except InvalidCoordinateInputError as e:
        print(e)
    except InvalidMove as e:
        print(e)
    except Exception as e:
        print("error", e)


if __name__ == '__main__':
    main()