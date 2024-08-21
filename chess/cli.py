from chess.chess import Chess

def main():
    chess = Chess()
    while chess.is_playing():
        play(chess)

def play(chess):
    try:
        print(chess.show_board())
        print("turn: ", chess.turn)
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        to_row = int(input("To Row: "))
        to_col = int(input("To Col: "))

        chess.move(                                #para decir desde cual casilla hasta cual casilla (movimientos)
            from_row,
            from_col,
            to_row,
            to_col
        )

            
        piece = self.__board__.get_piece(from_row, from_col)          # Obtener la pieza en la posición de origen y verificar que existe
        if piece is None:
            raise ValueError("No existe una pieza en esa posición.")


        if (self.__turn__ == "WHITE" and piece.color == "BLACK") or (self.__turn__ == "BLACK" and piece.color == "WHITE"):     #turnos
            raise ValueError("No es tu turno.")
   
    
    except ValueError as e:                 #hago excepciones que garanticen que el camino esta bien
        print(f"Error: {e}")
        return False


    except Excepcion as e:
        print ('error')


if __name__ == '__main__':
    main()
