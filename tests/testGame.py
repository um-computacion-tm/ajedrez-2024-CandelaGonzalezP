"""import unittest
from chess.game import Chess
from chess.exceptions import *
from chess.board import Board
from unittest.mock import MagicMock, patch

class TestChess(unittest.TestCase):

    def setUp(self):
        self.chess = Chess()  # Inicializa un nuevo juego de ajedrez
        self.chess.__turn__ = "White"  # Establece el turno en blanco
        self.chess.__board__ = MagicMock()  # Simula el tablero

        self.piece = MagicMock()

    def test_is_playing(self):
        self.assertTrue(self.chess.is_playing())  # Verifica que is_playing retorne True

    def test_move_valid(self):
        self.assertEqual(self.chess.turn, "White")  # Verifica el turno inicial
        self.chess.__board__.get_piece.return_value = self.piece  # Simula una pieza en el tablero

        with self.assertRaises(InvalidMove):  # Intenta realizar un movimiento inválido
            self.chess.move(7, 2, 5, 4)  # Movimiento inválido

        self.assertEqual(self.chess.turn, "White")  # Verifica que el turno sigue siendo "white"


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
        self.assertEqual(str(context.exception), "No hay ninguna pieza en la posición de origen")  # Verifica el mensaje de la excepción

    def test_move_out_of_board(self):
        # Configura el mock para que devuelva una pieza al intentar obtener la pieza de la posición (1, 0)
        self.chess.__board__.get_piece.return_value = MagicMock()
        
        # Intentar mover a una posición fuera del tablero (8, 0)
        with self.assertRaises(DestinationInvalidMove) as context:
            self.chess.move(1, 0, 8, 0)  # Movimiento inválido hacia fuera del tablero
        self.assertEqual(str(context.exception), "Movimiento destino inválido")  # Verifica el mensaje de la excepción


    @patch.object(Chess, 'check_valid_move')
    @patch.object(Chess, 'check_turn')  # Mockea check_turn para evitar InvalidTurn
    def test_invalid_move(self, mock_check_turn, mock_check_valid_move):
        # Verifica que se lanza InvalidMove si el movimiento no es válido.
        from_row, from_col, to_row, to_col = 1, 1, 2, 2
        mock_check_turn.return_value = None  # Simula que el turno es válido
        mock_check_valid_move.side_effect = InvalidMove("Movimiento inválido")  # Simula un movimiento inválido

        with self.assertRaises(InvalidMove):
            self.chess.validate_move(self.piece, {'from_row': from_row, 'from_col': from_col, 'to_row': to_row, 'to_col': to_col})




if __name__ == '__main__':
    unittest.main()"""