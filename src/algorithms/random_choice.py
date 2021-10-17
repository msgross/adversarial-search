import math
import random

from src.algorithms.search import Search


class RandomChoice(Search):
    """ A random choice 'search' algorithm that just returns any of the available moves """
    def search(self, game, state, depth_remaining=math.inf, time_remaining=math.inf):
        """ Overrides Search.search """
        if game.is_terminal(state, True, True):
            return math.inf, None
        available_actions = game.actions(state)
        if len(available_actions) == 0:
            return math.inf, None
        random_move = random.choice(game.actions(state))
        random_score = game.eval(game.result(state, random_move))
        return random_score, random_move

