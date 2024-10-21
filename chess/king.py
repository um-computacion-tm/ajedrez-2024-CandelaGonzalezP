from chess.pieces import Piece        #REY 

class King(Piece):

    """
    Clase que representa un rey en el juego de ajedrez.
    
    Hereda de la clase Piece, lo que proporciona las funcionalidades básicas 
    para las piezas del juego.
    """

    def symbol(self):

        """
        Obtiene el símbolo que representa al rey.

        Returns:
            str: El símbolo del rey en función de su color ("♔" para blancas, "♚" para negras).
        """

        return '♔' if self.get_color() == 'WHITE' else '♚'

# Movimientos de a una casilla en todas las direcciones

    def valid_positions(self, from_row, from_col, to_row, to_col):

        if not self.is_within_board(to_row, to_col):
            return False 
        directions = self._king_queen_directions_
        possible_positions = self.get_possible_moves(from_row, from_col, directions)
        return (to_row, to_col) in possible_positions


    def get_possible_moves(self, from_row, from_col, directions):

        """
        Obtiene las posiciones válidas del rey desde una posición inicial.

        Args:
            from_row (int): Fila de la posición inicial.
            from_col (int): Columna de la posición inicial.
            directions (list): Lista de direcciones en las que el rey puede moverse.

        Returns:
            list: Lista de posiciones válidas a las que el rey puede moverse.
        """

        return self.find_valid_moves(from_row, from_col, directions, single_step=True)  
