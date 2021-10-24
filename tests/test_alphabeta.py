from unittest import TestCase
from algorithms.alphabeta import AlphaBeta
from tests._tree_example import eval_side_effect
from tests._tree_example import terminal_side_effect
from tests._tree_example import actions_side_effect
from tests._tree_example import result_side_effect


class TestAlphaBeta(TestCase):
    """ Define a graph we know the answer to, make sure we hit the right answer
        This is the same test as the one used in minimax, because both should
        probably come to the same answer in this case
                                          a
                                 a1   /---|----\    a3
                              /-------    |     -------\
                          ----         a2 |             ----
                          |               |                |
                          |               |                |
                        3 b             3 c              4 d
                        /-|-\            /|\              /|\
                    b1 /  |  \ b3       / | \ c3     d1  / | \ d3
                      / b2|   \      c1/  |  \          /  |  \
                     /    |    \      / c2|   \        / d2|   \
                    /     |     \    /    |    \      /    |    \
                   -             -  -           -    -     |     -
                 3 e    12f    8 g  2 h   4i    6j   14k   5l    2m
        Note that node k, with a score of 14 doesn't get selected. This is because
        we assume that the opponent is trying to pick the optimal means to minimize
        the score, so we take the conservative route of picking a1 since it has the
        'least worst' outcome

        If you were to adjust node m to have a terminal value of 3, it would still
        return the a1, even if there's a greater potential node if we took a3, since
        we assume the opponent will select the optimal move on their end, they're
        equivalent


    """
    def setUp(self):
        self.minimax_search = AlphaBeta()

    def test_search_from_root(self):
        """ Simple case, start from the root and return the expected minimax solution
        :return: pass if minimax alg traverses path as expected
        """
        value, move = self.minimax_search.search("a", terminal_side_effect, result_side_effect,
                                                 actions_side_effect, eval_side_effect)
        self.assertEqual("a1", move, "This graph should determine a1 to be the optimal move")
        self.assertEqual(3, value, "Valuation of this move is 3")

    def test_search_near_terminal(self):
        """ Simple case, start one one of root's children nodes and return the expected minimax solution
        :return: pass if minimax alg traverses path as expected
        """
        value, move = self.minimax_search.search("b", terminal_side_effect, result_side_effect,
                                                 actions_side_effect, eval_side_effect)
        self.assertEqual("b2", move, "Starting at node b should just return the move to the maximum leaf node")
        self.assertEqual(12, value, "Valuation of this move is 12")

    def test_search_at_terminal(self):
        """ Simple case, start at a terminating node
        :return: pass if None is returned, since no moves exist in a terminating state
        """
        value, move = self.minimax_search.search("e", terminal_side_effect, result_side_effect,
                                                 actions_side_effect, eval_side_effect)
        self.assertIsNone(move)

    def test_search_at_depth_limit(self):
        """ Simple case, apply a depth limit to return a solution
        :return: pass if optimal move given a depth limit is selected
        """
        value, move = self.minimax_search.search("a", terminal_side_effect, result_side_effect,
                                                 actions_side_effect, eval_side_effect, 1)
        self.assertEqual("a3", move, "Depth limit means we should just end up picking our child max")
        self.assertEqual(4, value, "Max child node is b, with a value of 4")
