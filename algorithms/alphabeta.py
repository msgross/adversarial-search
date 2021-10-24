"""
An alpha-beta pruning search algorithm

This provides a pruning search that cuts short searches where possible when
nothing better could be possibly encountered
"""
from math import inf
from algorithms.search import Search


class AlphaBeta(Search):
    """ Implements a basic Alpha-Beta pruning search
        Meant to cut down on searches needed by keeping track
        of the min and max encountered in past branches
    """
    def _max_value(self, state, is_terminal_fn, state_result_fn, actions_fn, eval_fn,
                   depth_remaining, time_remaining,
                   alpha=-inf, beta=inf):
        """ Method returns a maximizing value in the state tree that surpasses the current
            beta value if there is one

        :param is_terminal_fn: a function that returns true when a termination condition
                                is fulfilled
        :param state_result_fn: a function that returns the next state given an action
        :param actions_fn: a function that returns available actions given a state
        :param eval_fn: a function that returns an evaluation score on a given state
        :param state: The current game state
        :param depth_remaining: The remaining depth to search
        :param time_remaining:  The remaining time
        :param alpha: the value of the most maximizing choice we've found--min searches should
                        at least reach this level
        :param beta: the value of the most minimizing choice we've found--max searches should
                    at most reach this level
        :return: value, move tuple that is maximizing
        """
        if is_terminal_fn(state, depth_remaining > 0, time_remaining > 0):
            return eval_fn(state), None
        best_value = -inf
        best_move = None
        for action in actions_fn(state):
            state_after_action = state_result_fn(state, action)
            value, move = self._min_value(state_after_action,
                                          is_terminal_fn, state_result_fn, actions_fn, eval_fn,
                                          depth_remaining-1, time_remaining,
                                          alpha, beta)
            if value > best_value:
                best_value = value
                best_move = action
                alpha = max(alpha, best_value)
            if best_value >= beta:
                return best_value, best_move
        return best_value, best_move

    def _min_value(self, state, is_terminal_fn, state_result_fn, actions_fn, eval_fn,
                   depth_remaining, time_remaining,
                   alpha=-inf, beta=inf):
        """ Method returns a minimizing value in the state tree that surpasses the current
            alpha value if there is one

        :param is_terminal_fn: a function that returns true when a termination condition
                                is fulfilled
        :param state_result_fn: a function that returns the next state given an action
        :param actions_fn: a function that returns available actions given a state
        :param eval_fn: a function that returns an evaluation score on a given state
        :param state: The current game state
        :param depth_remaining: The remaining depth to search
        :param time_remaining:  The remaining time
        :param alpha: the value of the most maximizing choice we've found--min searches should
                        at least reach this level
        :param beta: the value of the most minimizing choice we've found--max searches should
                        at most reach this level
        :return: value, move tuple that is maximizing
        """
        if is_terminal_fn(state, depth_remaining > 0, time_remaining > 0):
            return eval_fn(state), None
        best_value = inf
        best_move = None
        for action in actions_fn(state):
            state_after_action = state_result_fn(state, action)
            value, move = self._max_value(state_after_action,
                                          is_terminal_fn, state_result_fn, actions_fn, eval_fn,
                                          depth_remaining-1, time_remaining,
                                          alpha, beta)
            if value < best_value:
                best_value = value
                best_move = action
                beta = min(beta, best_value)
            if best_value <= alpha:
                return best_value, best_move
        return best_value, best_move

    def search(self, state, is_terminal_fn, state_result_fn, actions_fn, eval_fn,
               depth_remaining=inf, time_remaining=inf):
        """ Overrides Search.search """
        return self._max_value(state, is_terminal_fn, state_result_fn, actions_fn, eval_fn,
                               depth_remaining, time_remaining)
