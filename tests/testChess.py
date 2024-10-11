"""
import unittest
from chess.chess import Chess
from chess.exceptions import *
from chess.board import Board
from unittest.mock import MagicMock

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()  # Inicializa un nuevo juego de ajedrez
        self.chess.__turn__ = "White"  # Establece el turno en blanco
        self.chess.__board__ = MagicMock()  # Simula el tablero


    def test_is_playing(self):
        self.assertTrue(self.chess.is_playing())  # Verifica que is_playing retorne True


    def test_move_valid(self):
        self.assertEqual(self.chess.turn, "White")        # Verifica el turno inicial
        with self.assertRaises(InvalidMove):        # Intenta realizar un movimiento inválido
            self.chess.move(7, 2, 5, 4)  # Movimiento inválido
        self.assertEqual(self.chess.turn, "White")        # Verifica que el turno sigue siendo "white" (no cambió)


    def test_change_turn(self):
        # Verifica el turno inicial
        self.assertEqual(self.chess.turn, "White")
        # Cambia el turno
        self.chess.change_turn()
        # Verifica que el turno cambió a 'black'
        self.assertEqual(self.chess.turn, "white")
        # Cambia el turno de nuevo
        self.chess.change_turn()
        # Verifica que el turno cambió de nuevo a 'white'
        self.assertEqual(self.chess.turn, "black")


    def test_ganador_when_opponent_has_no_pieces(self):
        self.chess.__board__.count_pieces.return_value = 0  # Simula que no quedan piezas del oponente
        result = self.chess.ganador()  # Llama al método
        self.assertTrue(result)  # Verifica que retorna True cuando el oponente no tiene piezas


    def test_ganador_when_opponent_has_pieces(self):
        self.chess.__board__.count_pieces.return_value = 1  # Simula que quedan piezas del oponente
        result = self.chess.ganador()  # Llama al método
        self.assertFalse(result)  # Verifica que retorna False cuando el oponente tiene piezas


    def test_move_empty_position(self):
        # Configura el mock para que devuelva None al intentar obtener la pieza de la posición (0, 0)
        self.chess.__board__.get_piece.return_value = None
        
        # Intentar mover desde una posición vacía (0, 0)
        with self.assertRaises(EmptyPosition) as context:
            self.chess.move(0, 0, 1, 0)  # Desde una posición vacía hacia (1, 0)
        self.assertEqual(str(context.exception), "La posicion esta vacia")  # Verifica el mensaje de la excepción

    def test_move_out_of_board(self):
        # Configura el mock para que devuelva una pieza al intentar obtener la pieza de la posición (1, 0)
        self.chess.__board__.get_piece.return_value = MagicMock()
        
        # Intentar mover a una posición fuera del tablero (8, 0)
        with self.assertRaises(DestinationInvalidMove) as context:
            self.chess.move(1, 0, 8, 0)  # Movimiento inválido hacia fuera del tablero
        self.assertEqual(str(context.exception), "Movimiento inválido hacia la posición de destino")  # Verifica el mensaje de la excepción

if __name__ == '__main__':
    unittest.main()
"""
