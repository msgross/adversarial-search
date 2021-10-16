import math
from search import Search


class Minimax(Search):
    def _max_value(self, game, state, player):
        if game.isTerminal(state):
            return game.utility(state, player), None
        best_value = -math.inf
        best_move = None
        for action in game.actions(state):
            value, move = self._min_value(game, game.result(state, action))
            if value > best_value:
                best_value = value
                best_move = move
        return best_value, best_move

    def _min_value(self, game, state, player):
        if game.isTerminal(state):
            return game.utility(state, player), None
        best_value = math.inf
        best_move = None
        for action in game.actions(state):
            value, move = self._max_value(game, game.result(state, action))
            if value < best_value:
                best_value = value
                best_move = move
        return best_value, best_move

    def search(self, game, state, depth=math.inf, time_remaining=math.inf):
        pass
