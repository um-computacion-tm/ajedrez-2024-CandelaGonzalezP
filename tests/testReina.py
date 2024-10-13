import unittest
from chess.queen import Queen
from chess.board import Board
from unittest.mock import MagicMock

class TestQueenValidPositions(unittest.TestCase):

# Simbolos piezas reinas (blanco y negro)

    def test_queen_symbol_white(self):
        board = Board()
        queen = Queen("WHITE", board)
        self.assertEqual(queen.symbol(), 'Q')

    def test_queen_symbol_black(self):
        board = Board()
        queen = Queen("BLACK", board)
        self.assertEqual(queen.symbol(), 'q')

# Inicializar

    def setUp(self):
        self.board = MagicMock()
        self.white_queen = Queen("WHITE", self.board)

# Movimientos válidos (diagonal, vertical y horizontal)

    def test_valid_moves(self):
        self.board.get_piece.side_effect = lambda row, col: None
        
        # Verificamos varios movimientos válidos en diferentes direcciones
        self.assertTrue(self.white_queen.queen_valid_positions(3, 3, 4, 3))  # Abajo
        self.assertTrue(self.white_queen.queen_valid_positions(3, 3, 2, 3))  # Arriba
        self.assertTrue(self.white_queen.queen_valid_positions(3, 3, 3, 4))  # Derecha
        self.assertTrue(self.white_queen.queen_valid_positions(3, 3, 3, 2))  # Izquierda
        self.assertTrue(self.white_queen.queen_valid_positions(3, 3, 4, 4))  # Diagonal abajo derecha
        self.assertTrue(self.white_queen.queen_valid_positions(3, 3, 2, 2))  # Diagonal arriba izquierda

# Captura de piezas enemigas

    def test_capture_piece(self):
        mock_black_piece = MagicMock()
        mock_black_piece.get_color.return_value = "BLACK"
        self.board.get_piece.side_effect = lambda row, col: mock_black_piece if (row, col) == (5, 5) else None
        
        self.assertTrue(self.white_queen.queen_valid_positions(4, 4, 5, 5))  # Captura diagonal

# Movimiento inválido (bloqueado por una pieza del mismo color)

    def test_invalid_move(self):
        mock_white_piece = MagicMock()
        mock_white_piece.get_color.return_value = "WHITE"
        self.board.get_piece.side_effect = lambda row, col: mock_white_piece if (row, col) == (5, 5) else None
        
        self.assertFalse(self.white_queen.queen_valid_positions(4, 4, 5, 5))  # No puede capturar a una pieza del mismo color

# Restricción de movimiento a un solo paso

    def test_restrict_to_single_step(self):
        self.board.get_piece.side_effect = lambda row, col: None

    # Probar con una dirección y limitar el movimiento a un paso
    
        self.assertTrue(self.white_queen.queen_valid_positions(4, 4, 5, 4, directions=[(1, 0)]))  # Solo un paso adelante
        self.assertTrue(self.white_queen.queen_valid_positions(4, 4, 6, 4, directions=[(1, 0)]))  # Más de un paso no es válido

if __name__ == "__main__":
    unittest.main()






"""import unittest
from chess.queen import Queen
from chess.board import Board
from unittest.mock import MagicMock



class TestQueenOrthogonalMoves(unittest.TestCase):

# simbolos piezas reinas (blanco y negro)

    def test_queen_symbol_white(self):
        board = Board()
        queen = Queen("WHITE", board)
        self.assertEqual(queen.symbol(), 'Q')

    def test_queen_symbol_black(self):
        board = Board()
        queen = Queen("BLACK", board)
        self.assertEqual(queen.symbol(), 'q')

#movimientos validos

    def setUp(self):
        self.board = MagicMock()
        self.white_queen = Queen("White", self.board)

    def test_valid_moves(self):
        self.board.get_piece.side_effect = lambda row, col: None

        # Verifica movimientos válidos (diagonal, vertical y horizontal)
        valid_moves = self.white_queen.calculate_possible_moves(3, 3)
        expected_moves = [
            (4, 3), (2, 3),  # Abajo y Arriba
            (3, 4), (3, 2),  # Derecha e Izquierda
            (4, 4), (4, 2),  # Diagonal Abajo Derecha e Izquierda
            (2, 4), (2, 2),  # Diagonal Arriba Derecha e Izquierda
        ]
        self.assertTrue(all(move in valid_moves for move in expected_moves))

    def test_capture_piece(self):
        mock_black_piece = MagicMock()
        mock_black_piece.get_color.return_value = "Black"
        self.board.get_piece.side_effect = lambda row, col: mock_black_piece if (row, col) == (5, 5) else None
        valid_moves = self.white_queen.calculate_possible_moves(4, 4)
        self.assertIn((5, 5), valid_moves)  # La reina debe poder capturar en (5, 5)

    def test_invalid_move(self):
        mock_white_piece = MagicMock()
        mock_white_piece.get_color.return_value = "White"
        self.board.get_piece.side_effect = lambda row, col: mock_white_piece if (row, col) == (5, 5) else None
        valid_moves = self.white_queen.calculate_possible_moves(4, 4)
        self.assertNotIn((5, 5), valid_moves)  # La reina no debe poder moverse a (5, 5)


    def test_restrict_to_single_step(self):
        board = MagicMock()
        queen = Queen("White", board)
        board.get_piece.side_effect = lambda row, col: None

        valid_moves = queen._calculate_moves_in_directions(4, 4, [(1, 0)], restrict_to_single_step=True)
        self.assertEqual(valid_moves, [(5, 4)]) 


if __name__ == "__main__":
    unittest.main()"""