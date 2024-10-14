from chess.pieces import Piece      #PEON

class Pawn(Piece):

    """
    Clase que representa un peón en el juego de ajedrez.
    
    Hereda de la clase Piece, lo que proporciona las funcionalidades básicas 
    para las piezas del juego.
    """

    def symbol(self):

        """
        Obtiene el símbolo que representa al peón según su color.

        Returns:
            str: 'P' si el peón es blanco, 'p' si es negro.
        """

        return 'P' if self.get_color() == "WHITE" else 'p'

# Movimientos de avance y captura

    def pawns_valid_positions(self, from_row, from_col, to_row, to_col):

        """
        Verifica si la posición final del peón es válida.

        Args:
            from_row (int): Fila de la posición inicial del peón.
            from_col (int): Columna de la posición inicial del peón.
            to_row (int): Fila de la posición final del peón.
            to_col (int): Columna de la posición final del peón.

        Returns:
            bool: True si la posición final es válida, False en caso contrario.

        Description:
            Esta función verifica si el movimiento del peón desde (from_row, from_col) 
            hasta (to_row, to_col) es válido, considerando movimientos hacia adelante 
            y capturas diagonales.
        """

        valid_positions = []
        valid_positions.extend(self.get_forward_moves(from_row, from_col))
        valid_positions.extend(self.get_diagonal_captures(from_row, from_col))
        return (to_row, to_col) in valid_positions


    def get_forward_moves(self, from_row, from_col):

        """
        Obtiene los movimientos válidos hacia adelante del peón.

        Args:
            from_row (int): Fila de la posición inicial del peón.
            from_col (int): Columna de la posición inicial del peón.

        Returns:
            list: Lista de posiciones válidas hacia adelante que puede mover el peón.

        Description:
            Esta función calcula las posiciones válidas hacia adelante desde 
            (from_row, from_col) hasta que encuentre una pieza en el camino.
        """

        forward_moves = self.get_initial_forward_moves(from_row)
        valid_positions = []
        for move in forward_moves:
            next_row, next_col = from_row + move[0], from_col + move[1]
            if self.is_valid_move(next_row, next_col):
                valid_positions.append((next_row, next_col))
            else:
                break  # Detenerse si hay una pieza en el camino
        return valid_positions

    def get_initial_forward_moves(self, from_row):

        """
        Obtiene los movimientos válidos hacia adelante del peón.

        Args:
            from_row (int): Fila de la posición inicial del peón.
            from_col (int): Columna de la posición inicial del peón.

        Returns:
            list: Lista de posiciones válidas hacia adelante que puede mover el peón.

        Description:
            Esta función calcula las posiciones válidas hacia adelante desde 
            (from_row, from_col) hasta que encuentre una pieza en el camino.
        """

        forward_moves = [(1, 0)] if self.__color__ == "BLACK" else [(-1, 0)]        
        if self.is_initial_position(from_row):
            forward_moves.append(self.get_double_step_move())
        
        return forward_moves

    def is_initial_position(self, from_row):

        """
        Verifica si el peón está en su posición inicial.

        Args:
            from_row (int): Fila de la posición del peón.

        Returns:
            bool: True si el peón está en su posición inicial, False en caso contrario.
        """

        return (self.__color__ == "BLACK" and from_row == 1) or (self.__color__ == "WHITE" and from_row == 6)

    def get_double_step_move(self):

        """
        Obtiene el movimiento de dos casillas hacia adelante del peón.

        Returns:
            tuple: Movimiento de dos casillas hacia adelante según el color del peón.
        """

        return (2, 0) if self.__color__ == "BLACK" else (-2, 0)

    def is_valid_move(self, row, col):

        """
        Verifica si el movimiento a una posición específica es válido.

        Args:
            row (int): Fila de la posición a verificar.
            col (int): Columna de la posición a verificar.

        Returns:
            bool: True si la posición es válida y no hay piezas, False en caso contrario.
        """

        return (0 <= row < 8 and 0 <= col < 8) and (self.__board__.get_piece(row, col) is None)


    def get_diagonal_captures(self, from_row, from_col):

        """
        Obtiene las posiciones válidas para capturas diagonales del peón.

        Args:
            from_row (int): Fila de la posición inicial del peón.
            from_col (int): Columna de la posición inicial del peón.

        Returns:
            list: Lista de posiciones válidas para capturas diagonales.

        Description:
            Esta función verifica las posiciones diagonales donde el peón puede 
            capturar piezas enemigas.
        """

        diagonal_captures = [(1, 1), (1, -1)] if self.__color__ == "BLACK" else [(-1, 1), (-1, -1)]
        valid_positions = []
        for capture in diagonal_captures:
            next_row, next_col = from_row + capture[0], from_col + capture[1]
            if self.is_valid_capture(next_row, next_col):
                valid_positions.append((next_row, next_col))  # Solo se puede capturar si hay una pieza enemiga
        return valid_positions


    def is_valid_capture(self, row, col):

        """
        Verifica si una captura en una posición específica es válida.

        Args:
            row (int): Fila de la posición a verificar.
            col (int): Columna de la posición a verificar.

        Returns:
            bool: True si la captura es válida, False en caso contrario.
        """

        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        opponent_piece = self.__board__.get_piece(row, col)
        return opponent_piece and opponent_piece.get_color() != self.__color__
