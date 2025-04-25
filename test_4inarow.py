

import unittest
from unittest.mock import patch, Mock
from inarow import FourInARow

class TestGame(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.game = FourInARow()
        cls.game.board[0][0] = 'X'
        cls.game.board[0][1] = 'X'
        cls.game.board[0][2] = 'X'
        cls.game.board[0][3] = 'X'


    def test_entire_shortest_game_win(self):
        game = FourInARow()
        game.make_move(0)
        game.make_move(0)
        game.make_move(1)
        game.make_move(1)
        game.make_move(2)
        game.make_move(2)
        assert(game.make_move(3))


    def test_make_move(self):
        game = FourInARow()
        with patch.object(game, 'switch_players') as mock_switch_players:

            self.assertFalse(game.make_move(0))
            self.assertEqual(game.board, [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                                          ['X', ' ', ' ', ' ', ' ', ' ', ' ']])
            # raise Exception(Something went horrobly wrong)
            mock_switch_players.assert_called_once()

    def test_get_next_empty_row(self):
        game = FourInARow()
        game.board[5][0] = 'X'
        game.board[4][0] = 'O'
        game.board[3][0] = 'X'
        self.assertEqual(game.get_next_empty_row(0), 2)

    def test_check_horizontal_win(self):
        # Example for
        self.assertTrue(self.game.check_horizontal_win(0))

    def test_check_vertical_win(self):
        game = FourInARow()
        game.board[0][0] = 'X'
        game.board[1][0] = 'X'
        game.board[2][0] = 'X'
        game.board[3][0] = 'X'
        self.assertTrue(game.check_vertical_win(0))

    def test_check_positive_slope_diagonal_win(self):
        game = FourInARow()
        game.board[0][0] = 'X'
        game.board[1][1] = 'X'
        game.board[2][2] = 'X'
        game.board[3][3] = 'X'
        self.assertTrue(game.check_positive_slope_diagonal_win(3, 3))

    def test_check_negative_slope_diagonal_win(self):
        game = FourInARow()
        game.board[5][0] = 'X'
        game.board[4][1] = 'X'
        game.board[3][2] = 'X'
        game.board[2][3] = 'X'
        self.assertTrue(game.check_negative_slope_diagonal_win(2, 3))

    def test_check_tie(self):
        game = FourInARow()
        game.board = [['O', 'X', 'O', 'X', 'O', 'X', 'O'],
                      ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
                      ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
                      ['X', 'O', 'X', 'O', 'X', 'O', 'X'],
                      ['O', 'X', 'O', 'X', 'O', 'X', 'O'],
                      ['X', 'O', 'X', 'O', 'X', 'O', 'X']]
        self.assertTrue(game.check_tie())

    def test_switch_players(self):
        game = FourInARow()
        game.current_player = 'X'
        game.switch_players()
        self.assertEqual(game.current_player, 'O')
        game.switch_players()
        self.assertEqual(game.current_player, 'X')