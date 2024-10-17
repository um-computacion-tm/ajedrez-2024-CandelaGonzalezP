from chess.pieces import Piece        #REY 

class King(Piece):

    """
    Clase que representa un rey en el juego de ajedrez.
    
    Hereda de la clase Piece, lo que proporciona las funcionalidades básicas 
    para las piezas del juego.
    """

    def symbol(self):
        return '♔' if self.get_color() == 'WHITE' else '♚'

# Movimientos de a una casilla en todas las direcciones

    def king_valid_position(self, from_row, from_col, to_row, to_col):
        directions = self.__king_queen_directions__
        possible_positions = self.find_valid_moves(from_row, from_col, directions, single_step=True)
        return (to_row, to_col) in possible_positions
