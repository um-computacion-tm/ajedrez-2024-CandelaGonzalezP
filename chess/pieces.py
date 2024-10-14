class Piece:                       #HERENCIA PIEZAS 

   def __init__(self, color, board):
      
        """
        Inicializa una pieza de ajedrez.

        Args:
            color (str): Color de la pieza ('WHITE' o 'BLACK').
            board (Board): Objeto que representa el tablero de ajedrez.
        """

        self.__color__ = color
        self.__board__ = board
        self.__king_queen_directions__ = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]

   def symbol(self):
       
        """
        Devuelve un símbolo que representa la pieza. Este método debe ser sobrescrito en las subclases.

        Raises:
            NotImplementedError: Si no se implementa en la subclase.
        """

        raise NotImplementedError

   def get_color(self):
      
        """
        Retorna el color de la pieza.

        Returns:
            str: Color de la pieza ('WHITE' o 'BLACK').
        """

        return self.__color__


   def find_valid_moves(self, row, col, directions, single_step=False):
        
        """
        Encuentra movimientos válidos para la pieza en función de las direcciones dadas.

        Args:
            row (int): Fila de la posición actual.
            col (int): Columna de la posición actual.
            directions (list): Lista de tuplas que representan las direcciones de movimiento.
            single_step (bool): Si es True, solo permite un movimiento en una dirección.

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
        Explora en una dirección dada desde una posición inicial.

        Args:
            position (dict): Diccionario que contiene la fila y columna actuales.
            delta_row (int): Cambio en la fila para explorar.
            delta_col (int): Cambio en la columna para explorar.
            single_step (bool): Si es True, solo permite un paso en la dirección.

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
                break  # Si hay una pieza, se detiene el avance
            valid_moves.append((current_row, current_col))  
            if single_step:
                break  # Solo permite un paso si es necesario
            current_row, current_col = self.update_position(current_row, current_col, delta_row, delta_col)
        return valid_moves
        

   def handle_target_piece(self, target_piece, current_row, current_col, valid_moves):
        
        """
        Maneja la pieza objetivo en la posición actual.

        Args:
            target_piece (Piece): La pieza en la posición objetivo.
            current_row (int): Fila de la posición actual.
            current_col (int): Columna de la posición actual.
            valid_moves (list): Lista donde se almacenan los movimientos válidos.
        """

        if target_piece.get_color() != self.get_color():
            valid_moves.append((current_row, current_col))  

   def update_position(self, current_row, current_col, delta_row, delta_col):
        
        """
        Actualiza la posición actual según el cambio en fila y columna.

        Args:
            current_row (int): Fila actual.
            current_col (int): Columna actual.
            delta_row (int): Cambio en la fila.
            delta_col (int): Cambio en la columna.

        Returns:
            tuple: Nueva fila y columna después de aplicar el cambio.
        """

        return current_row + delta_row, current_col + delta_col


   def is_within_board(self, row, col):
      
        """
        Verifica si la posición dada está dentro de los límites del tablero.

        Args:
            row (int): Fila a verificar.
            col (int): Columna a verificar.

        Returns:
            bool: True si la posición está dentro del tablero, False en caso contrario.
        """

        return 0 <= row < 8 and 0 <= col < 8
