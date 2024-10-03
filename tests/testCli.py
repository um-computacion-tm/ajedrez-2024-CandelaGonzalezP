import unittest
from unittest.mock import patch, MagicMock
from chess.chess import Chess 
from chess.cli import play, main 
from chess.exceptions import *

class TestCli(unittest.TestCase):
    @patch(  
        'builtins.input',
        side_effect=['1', '1', '2', '2'], 
    )
    @patch('builtins.print') 
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
        self.assertEqual(mock_print.call_count, 2)  
        self.assertEqual(mock_chess_move.call_count, 1)

    


    @patch(  
        'builtins.input',
        side_effect=['hola', '1', '2', '2'], 
    )
    @patch('builtins.print') 
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
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 0)



    @patch(  
        'builtins.input',
        side_effect=['1', '1', '2', 'hola'],
    )
    @patch('builtins.print')
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




    @patch(  
        'builtins.input',
        side_effect=['1', '1', '2', '1'], 
    )
    @patch('builtins.print') # este patch controla lo que hace el print
    @patch.object(
        Chess,
        'move',
        side_effect=InvalidMove(),
    )

    def test_invalid_move(
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



    @patch("builtins.input", side_effect=["8","8","3","4"],)
    @patch("builtins.print")
    @patch.object(Chess,"move",side_effect=OriginInvalidMove())

    def test_invalid_origin_move(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ):

        chess = Chess()
        play(chess)
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 1)



    @patch("builtins.print")
    @patch("builtins.input",side_effect=["1","2","hola","2"])
    @patch.object(Chess,"move",side_effect=DestinationInvalidMove())

    def test_invalid_destination_move(
        self,
        mock_chess_move,
        mock_print,
        mock_input,
    ):
        chess=Chess()
        play(chess)
        self.assertEqual(mock_input.call_count,3)
        self.assertEqual(mock_print.call_count,4)
        self.assertEqual(mock_chess_move.call_count,0)


if __name__ == '__main__':
    unittest.main()

#patch --> sobreescribe el comportamiento de algo (cuando se agrega  un patch, el input no se ejecuta, directamentemente devuelve esos valores)
