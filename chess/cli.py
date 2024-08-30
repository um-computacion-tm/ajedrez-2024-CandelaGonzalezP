from chess.chess import Chess
from chess.exceptions import InvalidMove

def main():                                    #inicia un juego de ajedrez y ejecuta un bucle que sigue corriendo mientras el juego esté en curso 
    chess = Chess()
    while chess.is_playing():
        play(chess)

def play(chess):                         # muestra representacion del tablero, turno actual del jugador y pide al usuario que ingrese las filas y columnas de origen (from_row, from_col) y destino (to_row, to_col).
    try:
        print(chess.show_board())
        print("turn: ", chess.turn)
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To Row: "))
        to_col = int(input("To Col: "))

        chess.move(                                #especifica desde cual casilla hasta cual casilla (movimientos)
            from_row,
            from_col,
            to_row,
            to_col
        )
            
        piece = self.__board__.get_piece(from_row, from_col)          # Obtener la pieza en la posición de origen y verificar que existe
        if piece is None:
            raise ValueError("No existe una pieza en esa posición.")


        if (self.__turn__ == "WHITE" and piece.color == "BLACK") or (self.__turn__ == "BLACK" and piece.color == "WHITE"):     #verifica turnos
            raise ValueError("No es tu turno.")
   
    except Exception as e:            #Captura cualquier excepción que ocurra durante la ejecución del bloque try y muestra un mensaje de error con print("error", e).
        print("error", e)
    
if __name__ == '__main__':
    main()
