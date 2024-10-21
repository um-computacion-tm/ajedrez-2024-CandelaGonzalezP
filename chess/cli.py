import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from chess.game import Chess
from chess.exceptions import *

class ChessCli:

    def __init__(self):

        """
        Inicializa la interfaz de línea de comandos para el juego de ajedrez.

        Crea una instancia de la clase Chess que gestiona la lógica del juego.
        """

        self.__game__ = Chess()


    def start(self):

        """
        Inicia el juego de ajedrez.

        Muestra un mensaje de bienvenida y entra en un bucle que
        gestiona el flujo del juego hasta que se declare un ganador
        o se termine el juego.
        """

        print("¡Bienvenido al juego de Ajedrez!")
        while not self.__game__.is_game_over():
            self.show_board()
            print(f"Turno del jugador {self.__game__.get_turn()}")
            self.process_player_move()
            self.process_game_options()  

        self.end_game()

    def process_player_move(self):

        """
        Procesa el movimiento del jugador.

        Solicita al jugador que ingrese un movimiento y llama al método
        make_move() de la clase Chess. Muestra un mensaje de error si
        el movimiento es inválido.

        No recibe parámetros y no devuelve ningún valor.
        """

        move = self.get_move()
        if move:
            from_row, from_col, to_row, to_col = move
            try:
                self.__game__.make_move(from_row, from_col, to_row, to_col)
            except Exception as e:
                print(f"Error: {e}")

    def process_game_options(self):

        """
        Procesa las opciones adicionales del juego.

        Permite al jugador elegir entre salir del juego o ofrecer un empate.

        No recibe parámetros y no devuelve ningún valor.
        """

        option = self.offer_options()
        if option == 'exit':
            print("Has salido del juego.")
            raise SystemExit  # Salir del juego
        elif option == 'draw':
            print("Se ha ofrecido un empate.")



    def show_board(self):

        """
        Muestra el estado actual del tablero de ajedrez.

        No recibe parámetros y no devuelve ningún valor.
        """

        print(self.__game__.__board__)


    def get_move(self):

        """
        Obtiene el movimiento del jugador.

        Solicita al jugador que ingrese las coordenadas de la posición
        de origen y destino en formato fila,columna. 

        Returns:
            tuple: Una tupla que contiene las coordenadas (from_row, from_col, to_row, to_col) si la entrada es válida,
                   o llama nuevamente a sí mismo si la entrada es inválida.
        """

        try:
            from_pos = input("Ingrese la posición de origen (fila,columna): ")
            to_pos = input("Ingrese la posición de destino (fila,columna): ")
            from_row, from_col = map(int, from_pos.split(","))
            to_row, to_col = map(int, to_pos.split(","))
            return from_row, from_col, to_row, to_col
        except ValueError:
            print("Entrada inválida. Por favor ingrese en formato fila,columna.")
            return self.get_move()


    def offer_options(self):

        """
        Ofrece opciones adicionales al jugador.

        Permite al jugador ingresar la opción de salir del juego o
        ofrecer un empate. Si se ofrece un empate, el método solicita
        al otro jugador aceptar o rechazar la oferta.

        Returns:
            str: 'exit' si se desea salir del juego, 'draw' si se acepta el empate, o None si no se elige ninguna opción.
        """

        print()  
        exit_option = input("Ingrese 'exit' para salir del juego: ")
        if exit_option.lower() == 'exit':
            return 'exit' 

        draw_option = input("¿Ofrecer empate? (y/n): ")
        if draw_option.lower() == 'y':
            accept_draw = input("El otro jugador ofrece un empate. ¿Aceptar? (y/n): ")
            if accept_draw.lower() == 'y':
                print("El empate ha sido aceptado.")
                return 'draw' 
            else:
                print("El empate ha sido rechazado.")
        
        return None 
    

    def end_game(self):

        """
        Finaliza el juego y muestra el resultado.

        Anuncia que el juego ha terminado y muestra el ganador.
        
        No recibe parámetros y no devuelve ningún valor.
        """

        print("¡El juego ha terminado!")
        winner = "BLANCAS" if self.__game__.get_turn() == "BLACK" else "NEGRAS"
        print(f"El ganador es: {winner}")


if __name__ == "__main__":
    cli = ChessCli()
    cli.start()  # Inicia el juego