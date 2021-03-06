"""
Provides a random choice search algorithm

This random choice will just pick a random legal move to take
if one exists
"""
from math import inf
from random import choice
from algorithms.search import Search


class RandomChoice(Search):
    """ A random choice 'search' algorithm that just returns any of the available moves

        RandomChoice(state,depth, time) =
        {
            random(actions(state))
        }
    """
    def search(self, state, is_terminal_fn, state_result_fn, actions_fn, eval_fn,
               searched_nodes, depth_remaining=inf, time_remaining=inf):
        """ Overrides Search.search """
        if is_terminal_fn(state, True, True):
            return inf, None
        available_actions = actions_fn(state)
        if len(available_actions) == 0:
            return inf, None
        random_move = choice(available_actions)
        next_state = state_result_fn(state, random_move)
        random_score = eval_fn(next_state)
        searched_nodes.add_child(next_state)
        return random_score, random_move
