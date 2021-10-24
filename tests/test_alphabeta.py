from unittest import TestCase
from algorithms.alphabeta import AlphaBeta
from node import Node
from tests._tree_example import eval_side_effect
from tests._tree_example import terminal_side_effect
from tests._tree_example import actions_side_effect
from tests._tree_example import result_side_effect


class TestAlphaBeta(TestCase):
    """ Tests the alpha-beta pruning search algorithm

    """

    def setUp(self):
        self.search_alg = AlphaBeta()

    def test_search_from_root(self):
        """ Simple case, start from the root and return the expected minimax solution
        :return: pass if minimax alg traverses path as expected
        """
        root = Node("a")
        value, move = self.search_alg.search("a", terminal_side_effect, result_side_effect,
                                             actions_side_effect, eval_side_effect, root)
        self.assertEqual("a1", move, "This graph should determine a1 to be the optimal move")
        self.assertEqual(3, value, "Valuation of this move is 3")
        found_node = root.find("i")
        self.assertIsNone(found_node, "Alpha-Beta pruning should prune i and j states ")
        found_node = root.find("j")
        self.assertIsNone(found_node, "Alpha-Beta pruning should prune i and j states ")

    def test_search_near_terminal(self):
        """ Simple case, start one one of root's children nodes and return
            the expected minimax solution
        :return: pass if minimax alg traverses path as expected
        """
        root = Node("b")
        value, move = self.search_alg.search("b", terminal_side_effect, result_side_effect,
                                             actions_side_effect, eval_side_effect, root)
        self.assertEqual("b2", move,
                         "Starting at node b should just return the move to the maximum leaf node")
        self.assertEqual(12, value,
                         "Valuation of this move is 12")

    def test_search_at_terminal(self):
        """ Simple case, start at a terminating node
        :return: pass if None is returned, since no moves exist in a terminating state
        """
        root = Node("e")
        value, move = self.search_alg.search("e", terminal_side_effect, result_side_effect,
                                             actions_side_effect, eval_side_effect, root)
        self.assertIsNone(move)

    def test_search_at_depth_limit(self):
        """ Simple case, apply a depth limit to return a solution
        :return: pass if optimal move given a depth limit is selected
        """
        root = Node("a")
        value, move = self.search_alg.search("a", terminal_side_effect, result_side_effect,
                                             actions_side_effect, eval_side_effect, root, 1)
        self.assertEqual("a3", move, "Depth limit means we should just end up picking our child max")
        self.assertEqual(4, value, "Max child node is b, with a value of 4")
