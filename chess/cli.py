import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from chess.game import Chess
from chess.exceptions import *


def main():                                    
    chess = Chess()
    while chess.is_playing():
        play(chess)
 

def play(chess):
    try:
        print(chess.show_board()) 
        print("turn: ", chess.turn)
        print("Ingrese su movimiento, OFFER para empate o EXIT para terminar: ")

        from_row = input("Desde fila: ").strip().upper()

        # Opción para salir del juego
        if from_row == "EXIT":
            print(f"{chess.turn} ha terminado la partida.")
            exit()

        # Opción para ofrecer empate
        if from_row == "OFFER":
            print(f"{chess.turn} ha ofrecido un empate.")
            response = input("¿Aceptas el empate? (Y/N): ").strip().upper()
            if response == "Y":
                print("Ambos jugadores han acordado un empate. El juego ha terminado.")
                exit()  # Terminar el juego
            else:
                print("El jugador ha rechazado el empate. Continúa el juego.")
                return  # Regresa al inicio del turno actual

        from_col = input("Desde columna: ").strip().upper()
        if from_col == "EXIT":                      
            print(f"{chess.turn} ha terminado la partida.")
            exit()
        if from_col == "OFFER":
            print("El jugador ya ofreció el empate. Continúa con tu movimiento.")
            return  # Regresa al inicio del turno

        to_row = input("Hacia fila: ").strip().upper()
        if to_row == "EXIT":
            print(f"{chess.turn} ha terminado la partida.")
            exit()
        if to_row == "OFFER":
            print("El jugador ya ofreció el empate. Continúa con tu movimiento.")
            return  # Regresa al inicio del turno

        to_col = input("Hacia columna: ").strip().upper()
        if to_col == "EXIT":
            print(f"{chess.turn} ha terminado la partida.")
            exit()
        if to_col == "OFFER":
            print("El jugador ya ofreció el empate. Continúa con tu movimiento.")
            return  # Regresa al inicio del turno

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
            print(f"El juego ha terminado. {ganador} es el ganador.")
            exit()  # Salir del programa
        return

    # Manejar excepciones de manera ordenada
    except InvalidCoordinateInputError as e:
        print(e)
    except InvalidMove as e:
        print(e)
    except Exception as e:
        print("error", e)


if __name__ == '__main__':
    main()