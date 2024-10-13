from chess.chess import Chess
from chess.exceptions import *

def main():                                    
    chess = Chess()
    while chess.is_playing():
        play(chess)

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

