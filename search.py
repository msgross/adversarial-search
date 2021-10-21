import math
from algorithms.random_choice import RandomChoice
from game import Game


def search(game: Game, state, depth_remaining=math.inf, time_remaining=math.inf, search_fn=RandomChoice):
    """ Method executes a search lookup for a move to execute given a current state

    :param game: The game rules and conditions
    :param state: the current state of the game
    :param depth_remaining: the remaining depth to attempt to find an optimal move
    :param time_remaining: the remaining time to attempt to find an optimal move
    :param search_fn: the search function to apply for looking up a move
    :return: the value, move tuple of the selected move
    """
    return search_fn.search(game, state, depth_remaining, time_remaining)

