import unittest
from chess.exceptions import InvalidMove
from chess.exceptions import InvalidTurn
from chess.exceptions import EmptyPosition
from chess.exceptions import OutOfBoard

class TestExcepciones(unittest.TestCase):

    def test_invalid_move_message(self):
        exception = InvalidMove()
        self.assertEqual(str(exception), "Movimieto de pieza invalido")

    def test_invalid_turn_message(self):
        exception = InvalidTurn()
        self.assertEqual(str(exception), "No puedes mover pieza de otro jugador")

    def test_empty_position_message(self):
        exception = EmptyPosition()
        self.assertEqual(str(exception), "La posicion esta vacia")

    def test_out_of_board_message(self):
        exception = OutOfBoard()
        self.assertEqual(str(exception), "La posicion indicada se encuentra fuera del tablero")

if __name__ == '__main__':
    unittest.main()