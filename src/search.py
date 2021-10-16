import math
from src.algorithms.random_choice import RandomChoice


def search(game, state, depth=math.inf, time_remaining=math.inf, search_fn=RandomChoice):
    return search_fn.search(game, state, depth, time_remaining)

