import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from chess.exceptions import InvalidMove
from chess.exceptions import InvalidTurn
from chess.exceptions import EmptyPosition
from chess.exceptions import OutOfBoard
from chess.exceptions import OriginInvalidMove
from chess.exceptions import DestinationInvalidMove

class TestExcepciones(unittest.TestCase):

    def test_invalid_move_message(self):
        exception = InvalidMove()
        self.assertEqual(str(exception), "Movimiento inválido")

    def test_invalid_turn_message(self):
        exception = InvalidTurn()
        self.assertEqual(str(exception), "No es tu turno")

    def test_empty_position_message(self):
        exception = EmptyPosition()
        self.assertEqual(str(exception), "No hay ninguna pieza en la posición de origen")

    def test_out_of_board_message(self):
        exception = OutOfBoard()
        self.assertEqual(str(exception), "Movimiento fuera de tablero")

    def test_origin_invalid_move_message(self):
        exception = OriginInvalidMove()
        self.assertEqual(str(exception), "Sin piezas en posición origen")

    def test_destination_invalid_move_message(self):
        exception = DestinationInvalidMove()
        self.assertEqual(str(exception), "Movimiento destino inválido")

if __name__ == '__main__':
    unittest.main()