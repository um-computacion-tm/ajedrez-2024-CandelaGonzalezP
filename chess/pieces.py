class Piece:                       #HERENCIA PIEZAS 

   def __init__(self, color, board):
      self.__color__ = color
      self.__board__ = board
      self.__king_queen_directions__ = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]

   def symbol(self):
       """Devuelve un símbolo que representa la pieza. Este método se sobrescribirá en las subclases."""
       raise NotImplementedError   

   def get_color(self):
      return self.__color__


   def find_valid_moves(self, row, col, directions, single_step=False):
       valid_moves = []

       for delta_row, delta_col in directions:
        current_row, current_col = row + delta_row, col + delta_col
        
        while self.is_within_board(current_row, current_col):
            target_piece = self.__board__.get_piece(current_row, current_col)
            
            if target_piece is not None:
                if target_piece.get_color() != self.get_color():
                    valid_moves.append((current_row, current_col))  # Capturar pieza contraria
                break  # Si hay una pieza, se detiene el avance
                
            valid_moves.append((current_row, current_col))  # Movimiento vacío válido
            
            if single_step:
                break  # Solo permite un paso si es necesario
                
                # Continuar explorando en la misma dirección
            current_row += delta_row
            current_col += delta_col
        
       return valid_moves

   def is_within_board(self, row, col):
      return 0 <= row < 8 and 0 <= col < 8




"""
   def calculate_possible_moves(self, row, col, directions, single_step=False):
       possibles = []
       for row_dir, col_dir in directions:
           next_row, next_col = row + row_dir, col + col_dir
           while 0 <= next_row < 8 and 0 <= next_col < 8:
               other_piece = self.__board__.get_piece(next_row, next_col)
               if other_piece is not None:
                   if other_piece.get_color != self.get_color:
                    possibles.append((next_row, next_col))  # Puede capturar
                   break  # Detener si hay una pieza
               possibles.append((next_row, next_col))

                # Si `single_step` es True, solo avanzamos una casilla
               if single_step:
                    break

                # Continuar en la misma dirección
               next_row += row_dir
               next_col += col_dir
       return possibles
"""