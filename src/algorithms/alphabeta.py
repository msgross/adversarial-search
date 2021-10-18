import math
from search import Search


class AlphaBeta(Search):

    def _max_value(self, game, state, depth_remaining, time_remaining, alpha=-math.inf, beta=math.inf):
        if game.is_terminal(state, depth_remaining > 0, time_remaining > 0):
            return game.eval(state), None
        best_value = -math.inf
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

    def _min_value(self, game, state, depth_remaining, time_remaining,  alpha=-math.inf, beta=math.inf):

        if game.is_terminal(state, depth_remaining > 0, time_remaining > 0):
            return game.eval(state), None
        best_value = math.inf
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

    def search(self, game, state, depth_remaining=math.inf, time_remaining=math.inf):
        return self._max_value(game, state, depth_remaining, time_remaining)
