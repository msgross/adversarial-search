from math import inf
import random
from algorithms.search import Search


class RandomChoice(Search):
    """ A random choice 'search' algorithm that just returns any of the available moves

        RandomChoice(state,depth, time) =
        {
            random(actions(state))
        }
    """
    def search(self, game, state, depth_remaining=inf, time_remaining=inf):
        """ Overrides Search.search """
        if game.is_terminal(state, True, True):
            return inf, None
        available_actions = game.actions(state)
        if len(available_actions) == 0:
            return inf, None
        random_move = random.choice(game.actions(state))
        random_score = game.eval(game.result(state, random_move))
        return random_score, random_move

