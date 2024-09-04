import unittest
from chess.board import Board
from chess.knight import Knight

class TestKnight(unittest.TestCase):        #Configura el tablero y los caballos para las pruebas
    def setUp(self):
        self.board = Board(for_test=True)

    def test_knight_centro(self):        #Prueba los movimientos del caballo en el centro del tablero
        knight = Knight((4, 4), 'WHITE', self.board)
        self.board.set_piece(4, 4, knight)
        expected_moves = [
            (6, 5), (6, 3), (2, 5), (2, 3),
            (5, 6), (5, 2), (3, 6), (3, 2)
        ]
        moves = knight.get_possible_moves()
        self.assertCountEqual(moves, expected_moves)

    def test_knight_esquina(self):        #Prueba los movimientos del caballo en una esquina del tablero
        knight = Knight((0, 0), 'WHITE', self.board)
        self.board.set_piece(0, 0, knight)
        expected_moves = [(2, 1), (1, 2)]
        moves = knight.get_possible_moves()
        self.assertCountEqual(moves, expected_moves)

    def test_knight_bloqueado(self):        #Prueba los movimientos del caballo cuando está rodeado de piezas del mismo color
        knight = Knight((4, 4), 'WHITE', self.board)
        self.board.set_piece(4, 4, knight)
        
        for move in knight.get_possible_moves():        # Bloquear todas las posiciones posibles con piezas del mismo color
            self.board.set_piece(move[0], move[1], Knight(move, 'WHITE', self.board))
        moves = knight.get_possible_moves()
        self.assertEqual(moves, [])

    def test_knight_capturar(self):        #Prueba que el caballo puede capturar una pieza de color opuesto
        knight = Knight((4, 4), 'WHITE', self.board)
        self.board.set_piece(4, 4, knight)
        enemy_piece = Knight((6, 5), 'BLACK', self.board)        # Colocar una pieza de color opuesto en una de las posiciones posibles
        self.board.set_piece(6, 5, enemy_piece)
        moves = knight.get_possible_moves()        # Debe incluir el movimiento de captura
        self.assertIn((6, 5), moves)  


        
if __name__ == '__main__':
    unittest.main()
