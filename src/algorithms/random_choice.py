import math
import random

from src.algorithms.search import Search


class RandomChoice(Search):
    def search(self, game, state, depth_remaining=math.inf, time_remaining=math.inf):
        if game.is_terminal(state, True, True):
            return math.inf, None
        available_actions = game.actions(state)
        if len(available_actions) == 0:
            return math.inf, None
        return math.inf, random.choice(game.actions(state))

