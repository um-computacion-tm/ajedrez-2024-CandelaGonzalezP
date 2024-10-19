import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch, MagicMock
from chess.game import Chess
from chess.board import Board
from chess.king import King
from chess.queen import Queen
from chess.game import Chess
from chess.exceptions import *
from chess.cli import ChessCli

class TestChessCli(unittest.TestCase):

    @patch('builtins.print')  # Simular el print
    @patch.object(Chess, 'is_game_over', return_value=True)  # Simular que el juego termina
    def test_start_game_over(self, mock_is_game_over, mock_print):
        cli = ChessCli()  
        cli.start()  # Inicia el juego
        self.assertEqual(mock_print.call_count, 3)  # Se imprime el mensaje de inicio y fin de juego


    @patch('builtins.print')  # Simular el print
    @patch.object(Chess, 'get_turn', return_value="WHITE")  # Simular el turno del jugador
    def test_show_turn(self, mock_get_turn, mock_print):
        cli = ChessCli()
        cli.show_board()
        mock_print.assert_called_with(cli.__game__.__board__)  # Verificar que se muestra el tablero


if __name__ == "__main__":
    unittest.main()

