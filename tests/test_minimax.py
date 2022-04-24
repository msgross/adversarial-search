from unittest import TestCase
from algorithms.minimax import Minimax
from utils.node import Node
from tests._tree_example import eval_side_effect
from tests._tree_example import terminal_side_effect
from tests._tree_example import actions_side_effect
from tests._tree_example import result_side_effect


class TestMinimax(TestCase):
    """ Test the minimax search algorithm

    """
    def setUp(self):
        self.minimax_search = Minimax()

    def test_search_from_root(self):
        """ Simple case, start from the root and return the expected minimax solution
        :return: pass if minimax alg traverses path as expected
        """
        root = Node("a")
        value, move = self.minimax_search.search("a", terminal_side_effect, result_side_effect,
                                                 actions_side_effect, eval_side_effect, root)
        self.assertEqual("a1", move, "This graph should determine a1 to be the optimal move")
        self.assertEqual(3, value, "Valuation of this move is 3")

    def test_search_near_terminal(self):
        """ Simple case, start one one of root's children nodes and return the expected
            minimax solution
        :return: pass if minimax alg traverses path as expected
        """
        root = Node("b")
        value, move = self.minimax_search.search("b", terminal_side_effect, result_side_effect,
                                                 actions_side_effect, eval_side_effect, root)
        self.assertEqual("b2", move,
                         "Starting at node b should just return the move to the maximum leaf node")
        self.assertEqual(12, value, "Valuation of this move is 12")

    def test_search_at_terminal(self):
        """ Simple case, start at a terminating node
        :return: pass if None is returned, since no moves exist in a terminating state
        """
        root = Node("e")
        value, move = self.minimax_search.search("e", terminal_side_effect, result_side_effect,
                                                 actions_side_effect, eval_side_effect, root)
        self.assertIsNone(move)

    def test_search_at_depth_limit(self):
        """ Simple case, apply a depth limit to return a solution
        :return: pass if optimal move given a depth limit is selected
        """
        root = Node("a")
        value, move = self.minimax_search.search("a", terminal_side_effect, result_side_effect,
                                                 actions_side_effect, eval_side_effect, root, 1)
        self.assertEqual("a3", move,
                         "Depth limit means we should just end up picking our child max")
        self.assertEqual(4, value, "Max child node is b, with a value of 4")
