"""import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import unittest
from unittest.mock import patch, MagicMock
from chess.game import Chess
from chess.exceptions import *
from chess.cli import *



class TestCli(unittest.TestCase):

#MAIN 

    @patch('chess.cli.play')  # Parchear la función play para evitar la lógica real
    @patch('chess.game.Chess.is_playing', return_value=True)  # Simula que el juego está en curso
    def test_main(self, mock_is_playing, mock_play):
        mock_is_playing.side_effect = [True, False]  
        main()  # Llama a la función main
        self.assertEqual(mock_play.call_count, 1)





    @patch('builtins.input', side_effect=['hola', '0', '1', '0', 'EXIT'])
    @patch('builtins.print')  # Simular print
    @patch.object(Chess, 'move')
    def test_invalid_coordinate_input(self, mock_chess_move, mock_print, mock_input):
        chess = Chess()
        play(chess)
        # Verifica que el programa pidió 5 entradas
        self.assertEqual(mock_input.call_count, 4)
        # Verifica que el print se llamó 4 veces
        self.assertEqual(mock_print.call_count, 4)
        # Verifica que el movimiento no se ejecutó por entrada inválida
        self.assertEqual(mock_chess_move.call_count, 0)


    @patch('builtins.input', side_effect=['EXIT'])
    @patch('builtins.print')  # Simular print
    def test_exit_game(self, mock_print, mock_input):
        chess = MagicMock()  # Simular el objeto chess
        with self.assertRaises(SystemExit):  # Esperamos que el juego termine con "EXIT"
            play(chess)
        
        # Verifica que se imprimió el mensaje de salida
        mock_print.assert_any_call(f"{chess.turn} ha terminado la partida.")


    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['1', '1', '2', '2'], # estos son los valores que simula lo que ingresaria el usuario
    )
    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(Chess, 'move')
    def test_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): #
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 1)

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['hola', '1', '2', '2'], # estos son los valores que simula lo que ingresaria el usuario
    )
    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(Chess, 'move')
    def test_not_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): #
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 4)
        self.assertEqual(mock_chess_move.call_count, 0)

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['1', '1', '2', 'hola'], # estos son los valores que simula lo que ingresaria el usuario
    )
    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(Chess, 'move')
    def test_more_not_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): 
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 4)
        self.assertEqual(mock_chess_move.call_count, 0)


    @patch('builtins.input', side_effect=['OFFER', 'Y'])  # Simular la entrada para ofrecer empate y aceptar
    @patch('builtins.print')  # Simular print
    def test_accept_draw_offer(self, mock_print, mock_input):
        chess = MagicMock()  # Simular el objeto chess
        chess.turn = "WHITE"  # Establecer un turno ficticio
        
        with self.assertRaises(SystemExit):  # Esperamos que el juego termine al aceptar el empate
            play(chess)
        
        # Verifica que se imprimió el mensaje de aceptación de empate
        mock_print.assert_any_call("Ambos jugadores han acordado un empate. El juego ha terminado.")

    @patch('builtins.input', side_effect=['OFFER', 'N'])  # Simular la entrada para ofrecer empate y rechazar
    @patch('builtins.print')  # Simular print
    def test_reject_draw_offer(self, mock_print, mock_input):
        chess = MagicMock()  # Simular el objeto chess
        chess.turn = "BLACK"  # Establecer un turno ficticio
        
        play(chess)  # No esperamos que se lance una excepción aquí

        # Verifica que se imprimió el mensaje de rechazo de empate
        mock_print.assert_any_call("El jugador ha rechazado el empate. Continúa el juego.")


if __name__ == "__main__":
    unittest.main()"""