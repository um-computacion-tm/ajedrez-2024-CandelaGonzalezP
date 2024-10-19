import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from chess.game import Chess
from chess.exceptions import *

class ChessCli:

    def __init__(self):
        self.__game__ = Chess()

    def start(self):
        print("¡Bienvenido al juego de Ajedrez!")
        while not self.__game__.is_game_over():
            self.show_board()
            print(f"Turno del jugador {self.__game__.get_turn()}")
            from_row, from_col, to_row, to_col = self.get_move()
            try:
                self.__game__.make_move(from_row, from_col, to_row, to_col)
            except Exception as e:
                print(f"Error: {e}")
        self.end_game()


    def show_board(self):
        print(self.__game__.__board__)


    def get_move(self):
        try:
            from_pos = input("Ingrese la posición de origen (fila,columna): ")
            to_pos = input("Ingrese la posición de destino (fila,columna): ")
            from_row, from_col = map(int, from_pos.split(","))
            to_row, to_col = map(int, to_pos.split(","))
            return from_row, from_col, to_row, to_col
        except ValueError:
            print("Entrada inválida. Por favor ingrese en formato fila,columna.")
            return self.get_move()
        
    def end_game(self):
        print("¡El juego ha terminado!")
        winner = "BLANCAS" if self.__game__.get_turn() == "BLACK" else "NEGRAS"
        print(f"El ganador es: {winner}")


if __name__ == "__main__":
    cli = ChessCli()
    cli.start()  # Inicia el juego