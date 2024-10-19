from chess.pieces import Piece

class Queen(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        # Definimos las direcciones en las que la reina puede moverse: ortogonales y diagonales
        self.__queen_directions__ = [(-1, 0), (1, 0), (0, -1), (0, 1),  # Ortogonales (torre)
                                     (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonales (alfil)

    def symbol(self):
        """Devuelve el símbolo Unicode de la reina según el color."""
        return '♕' if self.get_color() == "WHITE" else '♛'

    def valid_positions(self, board, from_pos, to_pos):
        """Valida si el movimiento de la reina es correcto."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos

        # Verifica si el destino está dentro del tablero
        if not self.is_within_board(to_row, to_col):
            return False

        # Obtiene la pieza en la posición destino, si hay una
        target_piece = board.get_piece(to_row, to_col)

        # Si hay una pieza en la posición destino y es del mismo color, el movimiento no es válido
        if target_piece is not None and target_piece.get_color() == self.get_color():
            return False

        # Calcula los movimientos válidos en todas las direcciones posibles
        valid_moves = self.find_valid_moves(from_row, from_col, self.__queen_directions__)

        # Verifica si la posición destino está entre los movimientos válidos
        return (to_row, to_col) in valid_moves