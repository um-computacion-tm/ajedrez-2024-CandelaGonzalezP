import unittest
from chess.chess import Chess
#from chess.rook import Rook
#from chess.bishop import Bishop
#from chess.pawn import Pawn
#from chess.board import Board
from chess.exceptions import InvalidMove, InvalidTurn, EmptyPosition, OutOfBoard

class TestChess(unittest.TestCase):

    def test_is_playing(self):
        game = Chess()  # Inicializa un nuevo juego de ajedrez
        self.assertTrue(game.is_playing())  # Verifica que is_playing retorne True

    def setUp(self):
        self.game = Chess()  # Inicializa un nuevo juego de ajedrez

    def test_move_valid(self):
        self.game.move(7, 2, 5, 4)  # Realiza el movimiento
        self.assertEqual(self.game.turn, "white")        # Verifica que el turno cambió


    def test_change_turn(self):
        # Verifica el turno inicial
        self.assertEqual(self.game.turn, "WHITE")
        
        # Cambia el turno
        self.game.change_turn()
        # Verifica que el turno cambió a 'black'
        self.assertEqual(self.game.turn, "white")
        
        # Cambia el turno de nuevo
        self.game.change_turn()
        # Verifica que el turno cambió de nuevo a 'white'
        self.assertEqual(self.game.turn, "black")





if __name__ == '__main__':
    unittest.main()

