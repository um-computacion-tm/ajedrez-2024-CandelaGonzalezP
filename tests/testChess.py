import unittest
from chess.chess import Chess
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

    @patch('builtins.input', side_effect=['si'])  # Simula que el usuario ingresa "si"
    def test_offer_draw_accept(self, mock_input):
        with self.assertRaises(SystemExit):  # Espera que se llame a sys.exit()
            self.chess.offer_draw()  # Llama al método

    @patch('builtins.input', side_effect=['no'])  # Simula que el usuario ingresa "no"
    def test_offer_draw_reject(self, mock_input):
        result = self.chess.offer_draw()  # Llama al método
        self.assertTrue(result)  # Espera que la partida continúe

    @patch.object(Chess, 'check_valid_move')
    @patch.object(Chess, 'check_turn')  # Mockea check_turn para evitar InvalidTurn
    def test_check_valid_move_called(self, mock_check_turn, mock_check_valid_move):
        # Verifica que se llame a check_valid_move correctamente.
        from_row, from_col, to_row, to_col = 1, 1, 2, 2
        mock_check_valid_move.return_value = None  # Simula que el movimiento es válido
        mock_check_turn.return_value = None  # Simula que el turno es válido

        # Llama al método validate_move
        self.chess.validate_move(self.piece, {'from_row': from_row, 'from_col': from_col, 'to_row': to_row, 'to_col': to_col})

        # Verifica que check_valid_move fue llamado con los argumentos correctos
        mock_check_valid_move.assert_called_once_with(self.piece, {'from_row': from_row, 'from_col': from_col}, to_row, to_col)

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
    unittest.main()
