from unittest import TestCase
from mock import create_autospec
from src.game import Game
from src.algorithms.alphabeta import AlphaBeta
from math import inf


def terminal_side_effect(state, depth_remaining, time_remaining):
    """ Side effect returns true if we reach a terminal state

    :param state: the state of the game to evaluate
    :param depth_remaining: true if there is depth remaining
    :param time_remaining: true if there is time remaining
    :return: true if we are terminating
    """
    if not depth_remaining:
        return True
    end_state_nodes = []
    for alpha in list(map(chr, range(101, 110))):  # iterate from e-m
        end_state_nodes.append(str(alpha))
    if state in end_state_nodes:
        return True
    return False


def eval_side_effect(state):
    """ Side effect returns an evaluation given a state

    :param state: the current state to evaluate
    :return: a score for the current state
    """
    match state:
        case "a":
            return inf  # this is our root note, it shouldn't get a score
        case "b":
            return 3
        case "c":
            return 3
        case "d":
            return 4
        case "e":
            return 3
        case "f":
            return 12
        case "g":
            return 8
        case "h":
            return 2
        case "i":
            return 4
        case "j":
            return 6
        case "k":
            return 14
        case "l":
            return 5
        case "m":
            return 2
        case _:
            return -inf  # this shouldn't happen in our simple case


def actions_side_effect(state):
    """ Side effect for actions, returns the actions available for a given state

    :param state: the current state
    :return: actions available for the given state
    """
    match state:
        case "a":
            return ["a1", "a2", "a3"]
        case "b":
            return ["b1", "b2", "b3"]
        case "c":
            return ["c1", "c2", "c3"]
        case "d":
            return ["d1", "d2", "d3"]
        case "e":
            return []
        case "f":
            return []
        case "g":
            return []
        case "h":
            return []
        case "i":
            return []
        case "j":
            return []
        case "k":
            return []
        case "l":
            return []
        case "m":
            return []
        case _:
            return None  # This shouldn't happen


def result_side_effect(state, action):
    """ Side effect for result, returns the resulting state given an action

    :param state: the current state
    :param action: the action to take
    :return: the new state given the action
    """
    match action:
        # We would normally evaluate this with the
        # state to determine validity, etc, but this is a pre-established graph
        case "a1":
            return "b"
        case "a2":
            return "c"
        case "a3":
            return "d"
        case "b1":
            return "e"
        case "b2":
            return "f"
        case "b3":
            return "g"
        case "c1":
            return "h"
        case "c2":
            return "i"
        case "c3":
            return "j"
        case "d1":
            return "k"
        case "d2":
            return "l"
        case "d3":
            return "m"
        case _:
            return None  # default case, shouldn't happen


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
        self.mock_game = create_autospec(Game)
        self.mock_game.is_terminal.side_effect = terminal_side_effect
        self.mock_game.eval.side_effect = eval_side_effect
        self.mock_game.actions.side_effect = actions_side_effect
        self.mock_game.result.side_effect = result_side_effect
        self.minimax_search = AlphaBeta()

    def test_search_from_root(self):
        """ Simple case, start from the root and return the expected minimax solution
        :return: pass if minimax alg traverses path as expected
        """
        value, move = self.minimax_search.search(self.mock_game, "a")
        self.assertEqual("a1", move, "This graph should determine a1 to be the optimal move")
        self.assertEqual(3, value, "Valuation of this move is 3")

    def test_search_near_terminal(self):
        """ Simple case, start one one of root's children nodes and return the expected minimax solution
        :return: pass if minimax alg traverses path as expected
        """
        value, move = self.minimax_search.search(self.mock_game, "b")
        self.assertEqual("b2", move, "Starting at node b should just return the move to the maximum leaf node")
        self.assertEqual(12, value, "Valuation of this move is 12")

    def test_search_at_terminal(self):
        """ Simple case, start at a terminating node
        :return: pass if None is returned, since no moves exist in a terminating state
        """
        value, move = self.minimax_search.search(self.mock_game, "e")
        self.assertIsNone(move)

    def test_search_at_depth_limit(self):
        """ Simple case, apply a depth limit to return a solution
        :return: pass if optimal move given a depth limit is selected
        """
        value, move = self.minimax_search.search(self.mock_game, "a", 1)
        self.assertEqual("a3", move, "Depth limit means we should just end up picking our child max")
        self.assertEqual(4, value, "Max child node is b, with a value of 4")
