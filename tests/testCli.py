import unittest
from unittest.mock import patch, MagicMock
from chess.chess import Chess
from chess.exceptions import *
from chess.cli import handle_move_error, get_input_coordinates, play, main



class TestCli(unittest.TestCase):

#MAIN 

    @patch('chess.cli.play')  # Parchear la función play para evitar la lógica real
    @patch('chess.chess.Chess.is_playing', return_value=True)  # Simula que el juego está en curso
    def test_main(self, mock_is_playing, mock_play):
        mock_is_playing.side_effect = [True, False]  
        main()  # Llama a la función main
        self.assertEqual(mock_play.call_count, 1)


# GET INPUT COORDINATES

    @patch('builtins.input', side_effect=['2', '3'])  # Simula la entrada del usuario
    def test_get_input_coordinates_valid(self, mock_input):
        chess_mock = MagicMock()  # Crear un objeto simulado
        row, col = get_input_coordinates("From", chess_mock)
        self.assertEqual((row, col), (2, 3))  # Verifica que se retornen las coordenadas correctas

    @patch('builtins.input', side_effect=['stop'])  # Simula el comando para detener el juego
    def test_get_input_coordinates_stop(self, mock_input):
        chess_mock = MagicMock()  # Crear un objeto simulado
        row, col = get_input_coordinates("From", chess_mock)
        self.assertIsNone(row)  # Verifica que se retorne None para las coordenadas
        self.assertIsNone(col)


# HANDLE MOVE ERROR

    @patch('builtins.print')
    def test_handle_empty_position_error(self, mock_print):
        handle_move_error(EmptyPosition())
        mock_print.assert_called_once_with("No hay ninguna pieza en la posición de origen")


#PLAY

    @patch('builtins.print')
    @patch.object(Chess, 'move', side_effect=EmptyPosition())  # Simula la excepción EmptyPosition
    def test_play_empty_position_error(self, mock_move, mock_print):
        chess = Chess()
        with patch('chess.cli.get_input_coordinates', return_value=(0, 0)):
            play(chess)
            # Verifica que el mensaje de error fue impreso
            mock_print.assert_any_call("No hay ninguna pieza en la posición de origen")
            # También puedes verificar cuántas veces se llamó a print
            self.assertGreaterEqual(mock_print.call_count, 1)  # Al menos una llamada a print


    @patch('chess.cli.display_board')  # Parchear display_board para evitar su ejecución
    @patch('chess.cli.get_input_coordinates', return_value=(0, 0))  # Simular coordenadas de entrada
    @patch('builtins.print')  # Parchear print para verificar su llamada
    def test_play_unexpected_error(self, mock_print, mock_get_input_coordinates, mock_display_board):
        # Crear un mock para el objeto chess
        chess = MagicMock()
        chess.move.side_effect = Exception("Unexpected error")  # Lanzar una excepción genérica
        play(chess)
        # Verifica que se imprimió "Error inesperado"
        mock_print.assert_called_once_with("Error inesperado")  # Verificar que el mensaje se imprimió una vez



if __name__ == "__main__":
    unittest.main()