from math import inf
from src.algorithms.search import Search


class AlphaBeta(Search):
    """ Implements a basic Alpha-Beta pruning search
        Meant to cut down on searches needed by keeping track
        of the min and max encountered in past branches
    """
    def _max_value(self, game, state, depth_remaining, time_remaining, alpha=-inf, beta=inf):
        """ Method returns a maximizing value in the state tree that surpasses the current
            beta value if there is one

        :param game: The game, dictates game rules
        :param state: The current game state
        :param depth_remaining: The remaining depth to search
        :param time_remaining:  The remaining time
        :param alpha: the value of the most maximizing choice we've found--min searches should
                        at least reach this level
        :param beta: the value of the most minimizing choice we've found--max searches should at most reach
                        this level
        :return: value, move tuple that is maximizing
        """
        if game.is_terminal(state, depth_remaining > 0, time_remaining > 0):
            return game.eval(state), None
        best_value = -inf
        best_move = None
        for action in game.actions(state):
            state_after_action = game.result(state, action)
            value, move = self._min_value(game, state_after_action,
                                          depth_remaining-1, time_remaining,
                                          alpha, beta)
            if value > best_value:
                best_value = value
                best_move = action
                alpha = max(alpha, best_value)
            if best_value >= beta:
                return best_value, best_move
        return best_value, best_move

    def _min_value(self, game, state, depth_remaining, time_remaining,  alpha=-inf, beta=inf):
        """ Method returns a minimizing value in the state tree that surpasses the current
            alpha value if there is one

        :param game: The game, dictates game rules
        :param state: The current game state
        :param depth_remaining: The remaining depth to search
        :param time_remaining:  The remaining time
        :param alpha: the value of the most maximizing choice we've found--min searches should
                        at least reach this level
        :param beta: the value of the most minimizing choice we've found--max searches should at most reach
                        this level
        :return: value, move tuple that is maximizing
        """
        if game.is_terminal(state, depth_remaining > 0, time_remaining > 0):
            return game.eval(state), None
        best_value = inf
        best_move = None
        for action in game.actions(state):
            state_after_action = game.result(state, action)
            value, move = self._max_value(game, state_after_action,
                                          depth_remaining-1, time_remaining,
                                          alpha, beta)
            if value < best_value:
                best_value = value
                best_move = action
                beta = min(beta, best_value)
            if best_value <= alpha:
                return best_value, best_move
        return best_value, best_move

    def search(self, game, state, depth_remaining=inf, time_remaining=inf):
        """ Overrides Search.search """
        return self._max_value(game, state, depth_remaining, time_remaining)
