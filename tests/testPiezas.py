import unittest
from chess.pieces import Piece
from chess.board import Board
from chess.bishop import Bishop
from chess.pawn import Pawn
from chess.rook import Rook
from chess.queen import Queen
from unittest.mock import MagicMock

class TestPieces(unittest.TestCase):
    
    def test_get_color(self):
        piece = Piece("BLACK", None)  # Asume que la pieza necesita un color y el tablero
        self.assertEqual(piece.get_color(), "BLACK")

    def test_symbol_not_implemented(self):
        piece = Piece("WHITE", None)  # Crea una instancia de Piece
        with self.assertRaises(NotImplementedError):
            piece.symbol()  # Verifica que se lance NotImplementedError



if __name__ == '__main__':
    unittest.main()



