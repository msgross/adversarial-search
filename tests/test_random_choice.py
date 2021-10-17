from src.algorithms.random_choice import RandomChoice
from src.game import Game

import unittest
import mock


class TestRandomChoice(unittest.TestCase):

    def test_terminal_random_search(self):
        mock_game = mock.create_autospec(Game)
        mock_game.is_terminal.return_value = True
        mock_game.actions.return_value = []
        search = RandomChoice()
        start_state = [[0, 0]]
        value, move = search.search(mock_game, start_state)
        assert move is None

    def test_random_search(self):
        mock_game = mock.create_autospec(Game)
        mock_game.is_terminal.return_value = False
        mock_game.actions.return_value = [[0, 1], [1, 0]]
        search = RandomChoice()
        start_state = [[0, 0]]
        value, move = search.search(mock_game, start_state)
        assert move == [0, 1] or move == [1, 0]


if __name__ == '__main__':
    unittest.main()
