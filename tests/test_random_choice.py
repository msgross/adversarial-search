from unittest import TestCase
from mock import create_autospec
from math import inf
from src.algorithms.random_choice import RandomChoice
from src.game import Game


def result_state(state, action):
    """ side-effect method to return a simple resulting state given a preset
        selection of possible actions

    :param state: the current state -- unused
    :param action: the action to take, should just be [0,1] or [1,0] possible
    :return: the resulting state given the current state and action
    """

    if action == [0, 1]:
        return [[0, 1]]
    elif action == [1, 0]:
        return [[1, 0]]
    # This shouldn't happen in this test case
    return [[0, 0]]


def eval_state(state):
    """ side-effect method to return an evaluation score for the given state

    :param state: the current state to evaluate a score
    :return: should return 1 if the state is [[0,1]] or 0 if the state is [[1,0]].
             can return -1 if neither applies, but it shouldn't in this test case
    """
    if state == [[0, 1]]:
        return 1
    elif state == [[1, 0]]:
        return 0
    return -1


class TestRandomChoice(TestCase):
    """ Tests for the random choice 'search' option """

    def test_terminal_random_search(self):
        """ Tests result if random search is called when the game is already in a terminal
            state

        :return: success if the move selected is None with a score of infinity
        """
        mock_game = create_autospec(Game)
        mock_game.is_terminal.return_value = True
        mock_game.actions.return_value = []
        mock_game.eval.return_value = 1
        search = RandomChoice()
        start_state = [[0, 0]]
        value, move = search.search(mock_game, start_state)
        self.assertIsNone(move)
        self.assertEqual(inf, value, "Value of score must be inf")

    def test_random_search(self):
        """ Tests result when a random move is requested

        :return: success if one of the two possible moves are returned with the
                 appropriate score mapped
        """
        mock_game = create_autospec(Game)
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

