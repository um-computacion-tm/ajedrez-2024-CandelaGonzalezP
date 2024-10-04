import unittest
from chess.pieces import Piece
from chess.board import Board
from chess.bishop import Bishop
from chess.pawn import Pawn
from chess.rook import Rook

class TestPieces(unittest.TestCase):
    
    def test_get_color(self):
        piece = Piece("BLACK", None)  # Asume que la pieza necesita un color y el tablero
        self.assertEqual(piece.get_color(), "BLACK")

    def test_symbol_not_implemented(self):
        piece = Piece("WHITE", None)  # Crea una instancia de Piece
        with self.assertRaises(NotImplementedError):
            piece.symbol()  # Verifica que se lance NotImplementedError

    def test_valid_positions(self):
        piece = Piece("BLACK", None)
        piece.get_possible_positions = lambda x, y: [(3, 3)]  # Mockea los posibles movimientos
        self.assertTrue(piece.valid_positions(0, 0, 3, 3))

    def test_possible_diagonal_positions(self):
        piece = Piece("BLACK", None)
        self.assertEqual(piece.possible_diagonal_positions(0, 0), ())

    def test_possible_orthogonal_positions(self):
        piece = Piece("BLACK", None)
        piece.possible_positions_vd = lambda row, col: [(1, 0), (2, 0)]
        piece.possible_positions_va = lambda row, col: [(0, 1), (0, 2)]
        result = piece.possible_orthogonal_positions(0, 0)
        self.assertEqual(result, [(1, 0), (2, 0), (0, 1), (0, 2)])

    def test_possible_positions_vd(self):
        board = Board(for_test=True)
        piece = Piece("BLACK", board) 
        board.set_piece(3, 2, Piece("WHITE", board))  # Coloca una pieza de diferente color en la posición (3, 2)
        possibles = piece.possible_positions_vd(1, 2)
        self.assertEqual(possibles, [(2, 2), (3, 2)])       # Verifica que la función devuelve las posiciones hasta que encuentra una pieza blanca

    def test_possible_positions_va(self):
        board = Board(for_test=True)
        piece = Piece("BLACK", board) 
        possibles = piece.possible_positions_va(4, 2)
        self.assertEqual(possibles, [(3, 2), (2, 2), (1, 2), (0, 2)])        # Verifica que la función devuelve las posiciones hacia arriba desde la fila 4 en la columna 2


# para mejorar codigo

    def test_possible_positions_hl_with_opponent_piece(self):
        board = Board()
        rook = Rook("WHITE", board)
        board.set_piece(4, 4, rook)  # Colocar la torre en (4, 4)

        # Colocar un peón enemigo en la izquierda (4, 3)
        opponent_pawn = Pawn("BLACK", board)
        board.set_piece(4, 3, opponent_pawn)
        possibles = rook.possible_positions_hl(4, 4)
        self.assertEqual(possibles, [(4, 3)])


    def test_possible_positions_hl_with_own_piece(self):
        board = Board()
        rook = Rook("WHITE", board)
        board.set_piece(4, 4, rook)  # Colocar la torre en (4, 4)

        # Colocar un peón propio en la izquierda (4, 3)
        own_pawn = Pawn("WHITE", board)
        board.set_piece(4, 3, own_pawn)
        possibles = rook.possible_positions_hl(4, 4)
        self.assertEqual(possibles, [])


    def test_possible_positions_dad_no_obstacles(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)  # Colocar el alfil en (4, 4)

        possibles = bishop.possible_positions_dad(4, 4)
        expected = [(3, 5), (2, 6), (1, 7)]  # Posiciones esperadas sin obstáculos
        self.assertEqual(possibles, expected)


    def test_possible_positions_dai_no_obstacles(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)  # Colocar el alfil en (4, 4)

        possibles = bishop.possible_positions_dai(4, 4)
        expected = [(3, 3), (2, 2), (1, 1)]  # Posiciones esperadas sin obstáculos
        self.assertEqual(possibles, expected)


    def test_possible_positions_ddd_no_obstacles(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)  # Colocar el alfil en (4, 4)

        possibles = bishop.possible_positions_ddd(4, 4)
        expected = [(5, 5)]  # Posiciones esperadas sin obstáculos
        self.assertEqual(possibles, expected)


    def test_possible_positions_ddi_no_obstacles(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)  # Colocar el alfil en (4, 4)

        possibles = bishop.possible_positions_ddi(4, 4)
        expected = [(5, 3)]  # Posiciones esperadas sin obstáculos
        self.assertEqual(possibles, expected)


    def test_possible_positions_ddi_with_opponent_piece(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)  # Colocar el alfil en (4, 4)

        # Colocar un peón enemigo en la diagonal (5, 3)
        opponent_pawn = Pawn("BLACK", board)
        board.set_piece(5, 3, opponent_pawn)
        possibles = bishop.possible_positions_ddi(4, 4)
        self.assertEqual(possibles, [(5, 3)])

    def test_possible_positions_ddi_with_own_piece(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)  # Colocar el alfil en (4, 4)

        # Colocar un peón propio en la diagonal (5, 3)
        own_pawn = Pawn("WHITE", board)
        board.set_piece(5, 3, own_pawn)
        possibles = bishop.possible_positions_ddi(4, 4)
        self.assertEqual(possibles, [])

    def test_possible_positions_ddd_with_opponent_piece(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)  # Colocar el alfil en (4, 4)

        # Colocar un peón enemigo en la diagonal (5, 5)
        opponent_pawn = Pawn("BLACK", board)
        board.set_piece(5, 5, opponent_pawn)
        possibles = bishop.possible_positions_ddd(4, 4)
        self.assertEqual(possibles, [(5, 5)])

    def test_possible_positions_ddd_with_own_piece(self):
        board = Board()
        bishop = Bishop("WHITE", board)
        board.set_piece(4, 4, bishop)  # Colocar el alfil en (4, 4)

        # Colocar un peón propio en la diagonal (5, 5)
        own_pawn = Pawn("WHITE", board)
        board.set_piece(5, 5, own_pawn)
        possibles = bishop.possible_positions_ddd(4, 4)
        self.assertEqual(possibles, [])


if __name__ == '__main__':
    unittest.main()



