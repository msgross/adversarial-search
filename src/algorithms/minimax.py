import math
from search import Search


class Minimax(Search):
    def _max_value(self, game, state, player, depth_remaining, time_remaining):
        if game.is_terminal(state):
            return game.utility(state, player), None
        best_value = -math.inf
        best_move = None
        for action in game.actions(state):
            value, move = self._min_value(game, game.result(state, action), player,
                                          depth_remaining, time_remaining)
            if value > best_value:
                best_value = value
                best_move = move
        return best_value, best_move

    def _min_value(self, game, state, player, depth_remaining, time_remaining):
        if game.is_terminal(state):
            return game.utility(state, player), None
        best_value = math.inf
        best_move = None
        for action in game.actions(state):
            value, move = self._max_value(game, game.result(state, action), player,
                                          depth_remaining, time_remaining)
            if value < best_value:
                best_value = value
                best_move = move
        return best_value, best_move

    def search(self, game, state, depth_remaining=math.inf, time_remaining=math.inf):
        current_player = game.player_turn(state)
        value, move = self._max_value(game, state, current_player, depth_remaining, time_remaining)
        return move
