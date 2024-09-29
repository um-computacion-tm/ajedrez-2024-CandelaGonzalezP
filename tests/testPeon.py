import unittest
from chess.pawn import Pawn
from chess.board import Board


class TestPawn(unittest.TestCase):

# simbolos piezas alfiles (blanco y negro)

    def test_pawn_symbol_white(self):
        board = Board()
        pawn = Pawn("WHITE", board)
        self.assertEqual(pawn.symbol(), 'P')

    def test_pawn_symbol_black(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        self.assertEqual(pawn.symbol(), 'p')

# movimientos

    def test_initial_black(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)

        possibles = pawn.get_possible_positions(1, 5)
        self.assertEqual(
            possibles,
            [(2, 5), (3, 5)]
        )

    def test_not_initial_black(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)

        possibles = pawn.get_possible_positions(2, 5)
        self.assertEqual(
            possibles,
            [(3, 5)]
        )

    def test_eat_left_black(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)
        board.set_piece(3, 6, Pawn("WHITE", board))

        possibles = pawn.get_possible_positions(2, 5)
        self.assertEqual(
            possibles,
            [(3, 5), (3, 6)]
        )

    def test_initial_white(self):
        board = Board(for_test = True)
        pawn = Pawn("WHITE", board)

        possibles = pawn.get_possible_positions(6, 4)
        self.assertEqual(
            possibles,
            [(5, 4), (4, 4)]
        )

    def test_not_initial_white(self):
        board = Board(for_test = True)
        pawn = Pawn("WHITE", board)

        possibles = pawn.get_possible_positions(5, 4)
        self.assertEqual(
            possibles,
            [(4, 4)]
        )

    def test_not_initial_white_block(self):
        board = Board(for_test = True)
        pawn = Pawn("WHITE", board)
        board.set_piece(4, 4, Pawn("BLACK", board))

        possibles = pawn.get_possible_positions(5, 4)
        self.assertEqual(
            possibles,
            []
        )

    def test_not_initial_black_block(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)
        board.set_piece(5, 4, Pawn("BLACK", board))

        possibles = pawn.get_possible_positions(4, 4)
        self.assertEqual(
            possibles,
            []
        )

if __name__ == '__main__':
    unittest.main()


#movimiento peon negro inicial, movimiento peon blanco inicial
#movimientos no iniciales (codigo primera ver)
#comer piezas (diagonales) para ambos colores
#funcion comer y mover
# extend para unir metodos
# no se puede mover si hay una pieza adelante


#promote = hace que se convierta el peon al llegar al final, se cambie por una pieza