from unittest import TestCase
import mock
from math import inf
from src.algorithms.random_choice import RandomChoice
from src.game import Game


def result_state(state, action):
    if action == [0,1]:
        return [[0,1]]
    elif action == [1, 0]:
        return [[1, 0]]
    return [[0, 0]]


def eval_state(state):
    if state == [[0, 1]]:
        return 1
    elif state == [[1, 0]]:
        return 0
    return -1


class TestRandomChoice(TestCase):

    def test_terminal_random_search(self):
        mock_game = mock.create_autospec(Game)
        mock_game.is_terminal.return_value = True
        mock_game.actions.return_value = []
        mock_game.eval.return_value = 1
        search = RandomChoice()
        start_state = [[0, 0]]
        value, move = search.search(mock_game, start_state)
        self.assertIsNone(move)
        self.assertEqual(inf, value, "Value of score is mea")

    def test_random_search(self):
        mock_game = mock.create_autospec(Game)
        mock_game.is_terminal.return_value = False
        mock_game.actions.return_value = [[0, 1], [1, 0]]
        mock_game.result.side_effect = result_state
        mock_game.eval.side_effect = eval_state
        search = RandomChoice()
        start_state = [[0, 0]]
        value, move = search.search(mock_game, start_state)
        self.assertIs((move == [0, 1] or move == [1, 0]), True, "Should be a random move")
        if move == [0, 1]:
            self.assertEqual(value, 1, "Move to [0, 1] should be worth 1 pt")
        elif move == [1, 0]:
            self.assertEqual(value, 0, "Move to [1, 0] should be worth 0 pt")
        else:
            self.fail("Selected move doesn't exist")

