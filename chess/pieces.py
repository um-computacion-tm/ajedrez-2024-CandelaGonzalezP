class Piece:                                   # HERENCIA PIEZAS 

    def __init__(self, color, board):

        """
        Inicializa una pieza de ajedrez.

        Args:
            color (str): Color de la pieza ('WHITE' o 'BLACK').
            board (Board): Objeto que representa el tablero de ajedrez.
        """

        self.__color__ = color
        self.__board__ = board
        self._king_queen_directions_ = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]   

    def get_directions(self):

        """
        Obtiene las direcciones de movimiento específicas de la pieza.

        Returns:
            list: Lista de tuplas que representan las direcciones de movimiento.
        """        """
        Obtiene las direcciones de movimiento específicas de la pieza.

        Returns:
            list: Lista de tuplas que representan las direcciones de movimiento.
        """

        return []  

    def get_color(self):

        """
        Obtiene el color de la pieza.

        Returns:
            str: Color de la pieza ('WHITE' o 'BLACK').
        """

        return self.__color__



    def find_valid_moves(self, row, col, directions, single_step=False):

        """
        Encuentra todos los movimientos válidos para la pieza en una posición dada.

        Args:
            row (int): Fila de la posición de la pieza.
            col (int): Columna de la posición de la pieza.
            directions (list): Lista de direcciones de movimiento.
            single_step (bool): Indica si se debe limitar el movimiento a un solo paso.

        Returns:
            list: Lista de posiciones válidas a las que la pieza puede moverse.
        """
        
        valid_moves = []
        position = {'row': row, 'col': col} 
        for delta_row, delta_col in directions:
            valid_moves.extend(self.explore_direction(position, delta_row, delta_col, single_step))
        return valid_moves


    def explore_direction(self, position, delta_row, delta_col, single_step):

        """
        Explora una dirección específica y encuentra movimientos válidos.

        Args:
            position (dict): Diccionario con la posición actual ('row' y 'col').
            delta_row (int): Cambio de fila.
            delta_col (int): Cambio de columna.
            single_step (bool): Indica si se debe limitar el movimiento a un solo paso.

        Returns:
            list: Lista de movimientos válidos en la dirección explorada.
        """

        row, col = position['row'], position['col']
        current_row, current_col = row + delta_row, col + delta_col
        valid_moves = []
        while self.is_within_board(current_row, current_col):
            target_piece = self.__board__.get_piece(current_row, current_col)
            if target_piece is not None:
                self.handle_target_piece(target_piece, current_row, current_col, valid_moves)
                break 
            valid_moves.append((current_row, current_col)) 
            if single_step:
                break  
            current_row, current_col = self.update_position(current_row, current_col, delta_row, delta_col)
        return valid_moves



    def handle_target_piece(self, target_piece, current_row, current_col, valid_moves):

        """
        Maneja la lógica para una pieza objetivo en la posición especificada.

        Args:
            target_piece (Piece): La pieza en la posición actual.
            current_row (int): Fila de la posición de la pieza objetivo.
            current_col (int): Columna de la posición de la pieza objetivo.
            valid_moves (list): Lista donde se agregarán los movimientos válidos.
        """

        if target_piece.get_color() != self.get_color():
            valid_moves.append((current_row, current_col)) 



    def update_position(self, current_row, current_col, delta_row, delta_col):

        """
        Actualiza la posición actual en función de los cambios dados.

        Args:
            current_row (int): Fila actual.
            current_col (int): Columna actual.
            delta_row (int): Cambio de fila.
            delta_col (int): Cambio de columna.

        Returns:
            tuple: Nueva posición (fila, columna) actualizada.
        """

        return current_row + delta_row, current_col + delta_col


    def is_within_board(self, row, col):

        """
        Verifica si la posición está dentro de los límites del tablero.

        Args:
            row (int): Fila a verificar.
            col (int): Columna a verificar.

        Returns:
            bool: True si la posición está dentro de los límites, False de lo contrario.
        """

        return all(0 <= x < 8 for x in (row, col))


    def is_own_piece(self, target_piece):

        """
        Verifica si la pieza objetivo es del mismo color que esta pieza.

        Args:
            target_piece (Piece): La pieza a verificar.

        Returns:
            bool: True si la pieza objetivo es del mismo color, False de lo contrario.
        """        """
        Verifica si la pieza objetivo es del mismo color que esta pieza.

        Args:
            target_piece (Piece): La pieza a verificar.

        Returns:
            bool: True si la pieza objetivo es del mismo color, False de lo contrario.
        """

        return target_piece is not None and target_piece.get_color() == self.get_color()