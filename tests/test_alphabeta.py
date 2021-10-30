"""
Tests the alphabeta search algorithm for pruning while retaining
search effectiveness
"""

from unittest import TestCase
from math import inf
from algorithms.alphabeta import AlphaBeta
from algorithms.minimax import  Minimax
from utils.node import Node
from tests._tree_example import eval_side_effect
from tests._tree_example import terminal_side_effect
from tests._tree_example import actions_side_effect
from tests._tree_example import result_side_effect


def beta_pruning_terminal_state(state, depth_remaining, time_remaining):
    """ Terminal state returns True when we reach a terminal state,
    or when we run out of time or depth we're allowed to search

    :param state: The state to evaluate if it is in a terminal state
    :param depth_remaining: The remaining depth
    :param time_remaining: The time remaining
    :return: True if we hit a terminal or cut-off state, False otherwise
    """
    if depth_remaining <= 0 or time_remaining <= 0:
        return True
    end_state_nodes = []
    for alpha in list(map(chr, range(104, 112))):  # iterate from h-o
        end_state_nodes.append(str(alpha))
    if state in end_state_nodes:
        return True
    return False


def beta_pruning_eval(state):
    """ Create a scoring state where depending on our depth searched, we can
    end up picking the wrong move

    :param state: The state to evaluate for a score
    :return: score of the state
    """
    match state:
        case "b":
            val = 2
        case "c":
            val = 1
        case "d":
            val = 3
        case "e":
            val = 4
        case "f":
            val = 5
        case "g":
            val = 6
        case "h":
            val = 14
        case "i":
            val = 13
        case "j":
            val = 12
        case "k":
            val = 11
        case "l":
            val = 10
        case "m":
            val = 9
        case "n":
            val = 8
        case "o":
            val = 7
        case _:
            val = inf  # case a is our root, so it doesn't have a value
    return val


def beta_pruning_actions(state):
    """ Return actions available given a state, we're essentially creating
    a binary tree, where each parent has two nodes to choose from

    :param state: The current state
    :return: The available actions given the current state
    """
    match state:
        case "a":
            val = ["a1", "a2"]
        case "b":
            val = ["b1", "b2"]
        case "c":
            val = ["c1", "c2"]
        case "d":
            val = ["d1", "d2"]
        case "e":
            val = ["e1", "e2"]
        case "f":
            val = ["f1", "f2"]
        case "g":
            val = ["g1", "g2"]
        case _:
            val = []  # Cases e-m are leaves, so should have no possible actions
    return val


def beta_pruning_result(state, action):
    """ Given a current state and an action, return the resulting state


    :param state: The current state
    :param action: The action to take
    :return: The resulting state given a current state and an action
    """
    match action:
        # We would normally evaluate this with the
        # state to determine validity, etc, but this is a pre-established graph
        case "a1":
            val = "b"
        case "a2":
            val = "c"
        case "b1":
            val = "d"
        case "b2":
            val = "e"
        case "c1":
            val = "f"
        case "c2":
            val = "g"
        case "d1":
            val = "h"
        case "d2":
            val = "i"
        case "e1":
            val = "j"
        case "e2":
            val = "k"
        case "f1":
            val = "l"
        case "f2":
            val = "m"
        case "g1":
            val = "n"
        case "g2":
            val = "o"
        case _:
            val = None  # default case, shouldn't happen
    return val


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

    def test_beta_limit_shortcut(self):
        """ Create a test case that exercises the beta-limit pruning to avoid diving too deep

        :return: success if pruning occurs due to a beta-limit being surpassed
        """
        root = Node("a")
        value, move = self.search_alg.search("a", beta_pruning_terminal_state, beta_pruning_result,
                                             beta_pruning_actions, beta_pruning_eval, root)
        self.assertEqual("a1", move, "This graph should determine a1 to be the optimal move")
        self.assertEqual(12, value, "Valuation of this move is 3")
        found_node = root.find("g")
        self.assertIsNone(found_node, "Alpha-Beta pruning should prune g and n,o child states")
        found_node = root.find("n")
        self.assertIsNone(found_node, "Alpha-Beta pruning should prune g and n,o child states")
        found_node = root.find("o")
        self.assertIsNone(found_node, "Alpha-Beta pruning should prune g and n,o child states")

    def test_beta_limit_depth(self):
        """ Create a test case that exercises the beta-limit pruning to avoid diving too deep

        :return: success if pruning occurs due to a beta-limit being surpassed
        """
        root = Node("a")
        value, move = self.search_alg.search("a", beta_pruning_terminal_state, beta_pruning_result,
                                             beta_pruning_actions, beta_pruning_eval, root, 1)
        self.assertEqual("a1", move, "This graph should determine a1 to be the optimal move at depth 1")
        root = Node("a")
        value, move = self.search_alg.search("a", beta_pruning_terminal_state, beta_pruning_result,
                                             beta_pruning_actions, beta_pruning_eval, root, 2)
        self.assertEqual("a2", move, "This graph should determine a2 to be the optimal move at depth 2")
        root = Node("a")
        value, move = self.search_alg.search("a", beta_pruning_terminal_state, beta_pruning_result,
                                             beta_pruning_actions, beta_pruning_eval, root, 3)
        self.assertEqual("a1", move, "This graph should determine a1 to be the optimal move at depth 3")
        found_node = root.find("g")
        self.assertIsNone(found_node, "Alpha-Beta pruning should prune g and n,o child states")
        minimax_search = Minimax()
        minimax_value, minimax_move = minimax_search.search("a", beta_pruning_terminal_state,
                                                            beta_pruning_result,
                                                            beta_pruning_actions,
                                                            beta_pruning_eval, root, 3)
        self.assertEqual(minimax_value, value,
                         "Make sure minimax and alphabeta choose the same move, despite pruning")
        self.assertEqual(minimax_move, move,
                         "Make sure minimax and alphabeta choose the same move, despite pruning")
