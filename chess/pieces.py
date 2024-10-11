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


   def calculate_possible_moves(self, current_row, current_col, movement_directions, restrict_to_single_step=False):
       valid_moves = []
        
       for delta_row, delta_col in movement_directions:
           next_row, next_col = current_row + delta_row, current_col + delta_col
           while 0 <= next_row < 8 and 0 <= next_col < 8:
                target_piece = self.__board__.get_piece(next_row, next_col)
                
                if target_piece is not None:
                    if target_piece.get_color() != self.get_color():
                        valid_moves.append((next_row, next_col))  # Puede capturar
                    break  # Detenerse si hay una pieza en la posición
                
                valid_moves.append((next_row, next_col))  # Agregar movimiento válido

                # Si se restringe a un solo paso, salir del bucle
                if restrict_to_single_step:
                    break

                # Continuar en la misma dirección
                next_row += delta_row
                next_col += delta_col
                return valid_moves
