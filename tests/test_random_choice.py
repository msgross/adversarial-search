"""
Random tests are kind of a coin flip (get it?), on one hand, yeah I want to make sure it gets
covered, on the other, it's random, so it messes with what should be consistent...
"""

from unittest import TestCase
from math import inf
from algorithms.random_choice import RandomChoice


def result_state(state, action):
    """ side-effect method to return a simple resulting state given a preset
        selection of possible actions

    :param state: the current state -- unused
    :param action: the action to take, should just be [0,1] or [1,0] possible
    :return: the resulting state given the current state and action
    """
    return [action]


class TestRandomChoice(TestCase):
    """ Tests for the random choice 'search' option """

    def test_terminal_random_search(self):
        """ Tests result if random search is called when the game is already in a terminal
            state

        :return: success if the move selected is None with a score of infinity
        """
        search = RandomChoice()
        start_state = [[0, 0]]
        value, move = search.search(start_state, lambda state, depth_remains, time_remains: True,
                                    result_state, lambda state: [], lambda state: 1)
        self.assertIsNone(move)
        self.assertEqual(inf, value, "Value of score must be inf")

    def test_random_search(self):
        """ Tests result when a random move is requested

        :return: success if one of the two possible moves are returned with the
                 appropriate score mapped
        """
        search = RandomChoice()
        start_state = [[0, 0]]
        value, move = search.search(start_state, lambda s, d, t: False,
                                    result_state, lambda s: [[0, 1], [1, 0]], lambda state: 1)
        self.assertIs((move == [0, 1] or move == [1, 0]), True, "Should be a random move")
        self.assertEqual(value, 1, "Move should be worth 1 point")

