import math
from search import Search


class AlphaBeta(Search):

    def _max_value(self, game, state, player, alpha=-math.inf, beta=math.inf):
        if game.is_terminal(state):
            return game.utility(state, player), None
        best_value = -math.inf
        best_move = None
        for action in game.actions(state):
            value, move = self._min_value(game, game.result(state, action), alpha, beta)
            if value > best_value:
                best_value = value
                best_move = move
                alpha = max(alpha, best_value)
            if best_value >= beta:
                return best_value, best_move
        return best_value, best_move

    def _min_value(self, game, state, player, alpha=-math.inf, beta=math.inf):
        if game.is_terminal(state):
            return game.utility(state, player), None
        best_value = math.inf
        best_move = None
        for action in game.actions(state):
            value, move = self._max_value(game, game.result(state, action), alpha, beta)
            if value < best_value:
                best_value = value
                best_move = move
            if best_value <= alpha:
                return best_value, best_move
        return best_value, best_move

    def search(self, game, state, depth=math.inf, time_remaining=math.inf):
        current_player = game.player_turn(state)
        value, move = self._max_value(game, state, current_player)
        return move
