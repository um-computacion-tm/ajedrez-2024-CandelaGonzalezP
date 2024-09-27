class Piece:                       #HERENCIA PIEZAS 

   def __init__(self, color, board):
      self.__color__ = color
      self.__board__ = board

   def __str__(self):
      if self.__color__ == "WHITE":
         return self.white_str
      else:
         return self.black_str

   def get_color(self):
      return self.__color__

# MOVIMIENTOS POSIBLES

   def valid_positions(
      self,
      from_row,
      from_col,
      to_row,
      to_col,
   ):
      possible_positions = self.get_possible_positions(from_row, from_col)
      return (to_row, to_col) in possible_positions

# FUNCIONES DIAGONALES Y ORTOGONALES

   def possible_diagonal_positions(self, from_row, from_col):
      return ()
   
   def get_possible_positions(self, from_row, from_col):
      return self.possible_diagonal_positions(
          from_row,
          from_col,
      )

   def possible_orthogonal_positions(self, from_row, from_col):
      return (
         self.possible_positions_vd(from_row, from_col) +
         self.possible_positions_va(from_row, from_col)
      )

# MOVIMIENTOS VERTICALES ASCENDENTES Y DESCENDENTES

   def possible_positions_vd(self, row, col):
      possibles = []
      for next_row in range(row + 1, 8):
            # que la celda que sigue no este ocupada..
         other_piece = self.__board__.get_piece(next_row, col)
         if other_piece is not None:
               if other_piece.__color__ != self.__color__:
                  possibles.append((next_row, col))
               break
         possibles.append((next_row, col))
      return possibles

   def possible_positions_va(self, row, col):
      possibles = []
      for next_row in range(row - 1, -1, -1):
         possibles.append((next_row, col))
      return possibles
   
# MOVIMIENTOS HORIZONTALES DERECHA E IZQUIERDA

   def possible_positions_hr(self, row, col):
           possibles = []
           for next_col in range(col +1, 8):
               other_piece = self.__board__.get_piece(row, next_col)
               if other_piece is not None:
                   if other_piece.__color__ != self.__color__:
                       possibles.append((row, next_col))
                   break
               possibles.append((row, next_col))
           return possibles    
                

                
   def possible_positions_hl(self, row, col):
           possibles = []
           for next_col in range(col - 1, -1, -1):
               other_piece = self.__board__.get_piece(row, next_col)
               if other_piece is not None:
                   if other_piece.__color__ != self.__color__:
                       possibles.append((row, next_col))
                   break  
               possibles.append((row, next_col))
           return possibles



#MOVIMIENTOS DIAGONALES - diagonales ascendentes (derecha e izquierda) y descendentes (derecha e izquierda)


   def possible_positions_dad(self, row, col):  
       possibles = []
       next_row, next_col = row - 1, col + 1
       while next_row >= 0 and next_col < 8:
           other_piece = self.__board__.get_piece(next_row, next_col)
           if other_piece is not None:
               if other_piece.__color__ != self.__color__:
                   possibles.append((next_row, next_col))
               break
           possibles.append((next_row, next_col))
           next_row -= 1
           next_col += 1
       return possibles
    
   def possible_positions_dai(self, row, col):  # Diagonal ascendente izquierda
       possibles = []
       next_row, next_col = row - 1, col - 1
       while next_row >= 0 and next_col >= 0:
           other_piece = self.__board__.get_piece(next_row, next_col)
           if other_piece is not None:
               if other_piece.__color__ != self.__color__:
                   possibles.append((next_row, next_col))
               break
           possibles.append((next_row, next_col))
           next_row -= 1
           next_col -= 1
       return possibles
    
   def possible_positions_ddd(self, row, col):  # Diagonal descendente derecha
       possibles = []
       next_row, next_col = row + 1, col + 1
       while next_row < 8 and next_col < 8:
           other_piece = self.__board__.get_piece(next_row, next_col)
           if other_piece is not None:
               if other_piece.__color__ != self.__color__:
                   possibles.append((next_row, next_col))
               break
           possibles.append((next_row, next_col))
           next_row += 1
           next_col += 1
       return possibles

   def possible_positions_ddi(self, row, col):  # Diagonal descendente izquierda
       possibles = []
       next_row, next_col = row + 1, col - 1
       while next_row < 8 and next_col >= 0:
           other_piece = self.__board__.get_piece(next_row, next_col)
           if other_piece is not None:
               if other_piece.__color__ != self.__color__:
                   possibles.append((next_row, next_col))
               break
           possibles.append((next_row, next_col))
           next_row += 1
           next_col -= 1
       return possibles