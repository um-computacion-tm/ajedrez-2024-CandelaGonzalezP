from chess import Chess

def main():
    chess = Chess()
    while True:
        play(chess)

def play (chess):
    try:
        print(chess.show_board())     #muestro tablero
        from_row = int(input('From row: '))
        from_col = int(input('From col: '))
        to_row = int(input('To Row: '))
        to_col = int(input('To Col: '))

    #para decir desde cual casilla hasta cual casilla (movimientos)
        chess.move(          
            from_row,
            from_col,
            to_row,
            to_col
        )

    #hago excepciones que garanticen que el camino esta bien
    except Excepcion as e:
        print ('error')
