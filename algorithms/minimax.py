from math import inf
from algorithms.search import Search


class Minimax(Search):
    """ Minimax Search algorithm, basically portrays a state graph that assumes that
        both players are playing optimally. Maximizes score during maximizing turns,
        minimizes scoring during minimizing turns

        Minimax(state, depth, time) =
        {
            EVAL(state, depth, time)        if game is in a terminal state, or depth/time limit reached
            maximizing_action Minimax(Result(state, action), next_depth, next_time) if maximizing turn
            minimizing_action Minimax(Result(state, action), next_depth, next_time) if minimizing turn

        }
    """
    def _max_value(self, state, is_terminal_fn, state_result_fn, actions_fn, eval_fn,
                   depth_remaining, time_remaining):
        """ Method returns a maximizing value in the state tree, limited either
            by a terminal state or by reaching another cutoff limit

        :param is_terminal_fn: a function that returns true when a termination condition is fulfilled
        :param state_result_fn: a function that returns the next state given an action
        :param actions_fn: a function that returns available actions given a state
        :param eval_fn: a function that returns an evaluation score on a given state
        :param state: The current game state
        :param depth_remaining: Remaining depth before cutoff
        :param time_remaining: Remaining time before cutoff
        :return: tuple with maximized value and move
        """
        if is_terminal_fn(state, depth_remaining > 0, time_remaining > 0):
            return eval_fn(state), None
        best_value = -inf
        best_move = None
        for action in actions_fn(state):
            state_after_action = state_result_fn(state, action)
            value, move = self._min_value(state_after_action,
                                          is_terminal_fn, state_result_fn, actions_fn, eval_fn,
                                          depth_remaining-1, time_remaining)
            if value > best_value:
                best_value = value
                best_move = action
        return best_value, best_move

    def _min_value(self, state, is_terminal_fn, state_result_fn, actions_fn, eval_fn,
                   depth_remaining, time_remaining):
        """ Method returns a minimizing value in the state tree, limited either
            by a terminal state or by reaching another cutoff limit

        :param is_terminal_fn: a function that returns true when a termination condition is fulfilled
        :param state_result_fn: a function that returns the next state given an action
        :param actions_fn: a function that returns available actions given a state
        :param eval_fn: a function that returns an evaluation score on a given state
        :param state: The current game state
        :param depth_remaining: Remaining depth before cutoff
        :param time_remaining: Remaining time before cutoff
        :return: tuple with minimized value and move
        """
        if is_terminal_fn(state, depth_remaining > 0, time_remaining > 0):
            return eval_fn(state), None
        best_value = inf
        best_move = None
        for action in actions_fn(state):
            state_after_action = state_result_fn(state, action)
            value, move = self._max_value(state_after_action,
                                          is_terminal_fn, state_result_fn, actions_fn, eval_fn,
                                          depth_remaining-1, time_remaining)
            if value < best_value:
                best_value = value
                best_move = action
        return best_value, best_move

    def search(self, state, is_terminal_fn, state_result_fn, actions_fn, eval_fn,
               depth_remaining=inf, time_remaining=inf):
        """ Overrides Search.search """
        return self._max_value(state, is_terminal_fn, state_result_fn, actions_fn, eval_fn,
                               depth_remaining, time_remaining)
