import math
import random
from search import Search


class RandomChoice(Search):
    def search(self, game, state, depth_remaining=math.inf, time_remaining=math.inf):
        return math.inf, random.choice(game.actions(state))

