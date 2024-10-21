from chess.pieces import Piece                 #ALFIL

class Bishop(Piece):

    """
    Clase que representa un alfil en el juego de ajedrez.
    
    Hereda de la clase Piece, lo que proporciona las funcionalidades básicas 
    para las piezas del juego.
    """

    def symbol(self):

        """
        Devuelve el símbolo que representa al alfil en el tablero.

        Si la pieza es de color blanco, devuelve el símbolo correspondiente al alfil blanco ('♗').
        Si la pieza es de color negro, devuelve el símbolo correspondiente al alfil negro ('♝').

        Returns:
            str: El símbolo del alfil según su color ('♗' para blanco, '♝' para negro).
        """

        return '♗' if self.get_color() == 'WHITE' else '♝'


# Movimientos en diagonal

    def valid_positions(self, from_row, from_col, to_row, to_col):

        """
        Verifica si las coordenadas de destino están entre las posiciones válidas de movimiento del alfil.

        Utiliza la función `get_possible_moves` para obtener los movimientos posibles desde la posición inicial,
        y luego verifica si las coordenadas de destino están dentro de las posibles posiciones.

        Args:
            from_row (int): Fila de la posición de origen.
            from_col (int): Columna de la posición de origen.
            to_row (int): Fila de la posición de destino.
            to_col (int): Columna de la posición de destino.

        Returns:
            bool: True si la posición de destino es válida para el alfil, False en caso contrario.
        """

        available_moves = self.get_possible_moves(from_row, from_col)
        return (to_row, to_col) in available_moves

    def get_possible_moves(self, from_row, from_col):

        """
        Genera todas las posiciones válidas a las que el alfil puede moverse desde una posición dada.
        
        El alfil solo puede moverse en direcciones diagonales, por lo que se exploran las direcciones 
        (1,1), (-1,-1), (1,-1), (-1,1). Utiliza la función `find_valid_moves` para buscar posiciones válidas
        en esas direcciones.

        Args:
            from_row (int): Fila de la posición de origen.
            from_col (int): Columna de la posición de origen.

        Returns:
            list[tuple[int, int]]: Lista de tuplas que representan las coordenadas de las posiciones válidas
            a las que el alfil puede moverse.
        """

        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        return self.find_valid_moves(from_row, from_col, directions)
