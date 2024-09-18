import unittest
from unittest.mock import patch, MagicMock
from chess.chess import Chess
from chess.cli import play, main

class TestCli(unittest.TestCase):

    @patch(                                     # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['1', '1', '2', '2'],       # estos son los valores que simula lo que ingresaria el usuario
    )
    @patch('builtins.print')                    # este patch controla lo que hace el print
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

    @patch(                                                    # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['hola', '1', '2', '2'],                   # estos son los valores que simula lo que ingresaria el usuario
    )
    @patch('builtins.print')                                   # este patch controla lo que hace el print
    @patch.object(Chess, 'move')
    def test_not_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): #
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 1)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 0)

    @patch(                                                # este patch controla lo que hace el input
        'builtins.input',
        side_effect=['1', '1', '2', 'hola'],               # estos son los valores que simula lo que ingresaria el usuario
    )
    @patch('builtins.print')                               # este patch controla lo que hace el print
    @patch.object(Chess, 'move')
    def test_more_not_happy_path(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ): #
        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 0)


    @patch('chess.cli.play')  # Mock the play function to avoid user interaction
    @patch.object(Chess, 'is_playing', side_effect=[True, False])  # Mock is_playing to return True once and then False
    def test_main(self, mock_is_playing, mock_play):
        main()
        # Verify that play was called exactly once
        self.assertEqual(mock_play.call_count, 1)



if __name__ == '__main__':
    unittest.main()
 



#patch --> sobreescribe el comportamiento de algo (cuando se agrega  un patch, el input no se ejecuta, directamentemente devuelve esos valores)

