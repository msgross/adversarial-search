"""
Random tests are kind of a coin flip (get it?), on one hand, yeah I want to make sure it gets
covered, on the other, it's random, so it messes with what should be consistent...
"""
from unittest import TestCase
from math import inf
from algorithms.random_choice import RandomChoice


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
                                    lambda s, a: [a], lambda state: [], lambda state: 1)
        self.assertIsNone(move)
        self.assertEqual(inf, value, "Value of score must be inf")

    def test_no_legal_moves(self):
        """ Tests result if random search has no valid moves it can execute
        :return: success if the move seelcted is None with a score of infinity
        """
        search = RandomChoice()
        start_state = [[0,0]]
        value, move = search.search(start_state, lambda state, depth_remains, time_remains: False,
                                    lambda s, a: [], lambda state: [], lambda state: 1)
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
                                    lambda s, a: [a], lambda s: [[0, 1], [1, 0]], lambda state: 1)
        self.assertIs((move == [0, 1] or move == [1, 0]), True, "Should be a random move")
        self.assertEqual(value, 1, "Move should be worth 1 point")

