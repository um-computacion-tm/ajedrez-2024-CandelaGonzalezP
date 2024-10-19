from chess.pieces import Piece

class King(Piece):

    def __init__(self, color, board):
        super().__init__(color, board)
        # El rey puede moverse en todas las direcciones, pero solo una casilla a la vez
        self.__king_directions__ = [(-1, 0), (1, 0), (0, -1), (0, 1),   # Ortogonales
                                    (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonales

    def symbol(self):
        """Devuelve el símbolo Unicode del rey según el color."""
        return '♔' if self.get_color() == "WHITE" else '♚'

    def valid_positions(self, board, from_pos, to_pos):
        """Valida si el movimiento del rey es correcto."""
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

        # El rey solo se mueve una casilla en cualquier dirección
        if max(abs(from_row - to_row), abs(from_col - to_col)) > 1:
            return False

        # Calcula los movimientos válidos del rey
        valid_moves = self.find_valid_moves(from_row, from_col, self.__king_directions__, single_step=True)

        # Verifica si la posición destino está entre los movimientos válidos
        return (to_row, to_col) in valid_moves