from math import inf
from algorithms.random_choice import RandomChoice
from node import DummyNode


def search(state, is_terminal_fn, state_result_fn, actions_fn, eval_fn, searched_nodes,
           depth_remaining=inf, time_remaining=inf, search_fn=RandomChoice):
    """ Method executes a search lookup for a move to execute given a current state
    :param searched_nodes: returns a tree of searched nodes
    :param is_terminal_fn: a function that returns true when a termination condition is fulfilled
    :param state_result_fn: a function that returns the next state given an action
    :param actions_fn: a function that returns available actions given a state
    :param eval_fn: a function that returns an evaluation score on a given state
    :param state: the current state of the game
    :param depth_remaining: the remaining depth to attempt to find an optimal move
    :param time_remaining: the remaining time to attempt to find an optimal move
    :param search_fn: the search function to apply for looking up a move
    :return: the value, move tuple of the selected move
    """
    return search_fn.search(state, is_terminal_fn, state_result_fn, actions_fn, eval_fn,
                            searched_nodes, depth_remaining, time_remaining)


def search(state, is_terminal_fn, state_result_fn, actions_fn, eval_fn,
           depth_remaining=inf, time_remaining=inf, search_fn=RandomChoice):
    """
    See above, but retains an empty node that doesn't hold on to searched nodes information
    """
    return search_fn.search(state, is_terminal_fn, state_result_fn, actions_fn, eval_fn,
                            DummyNode(None), depth_remaining, time_remaining)
