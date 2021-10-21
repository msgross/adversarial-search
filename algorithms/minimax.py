from math import inf
from algorithms.search import Search
from game import Game


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
    def _max_value(self, game: Game, state, depth_remaining, time_remaining):
        """ Method returns a maximizing value in the state tree, limited either
            by a terminal state or by reaching another cutoff limit

        :param game: The game, dictate game rules
        :param state: The current game state
        :param depth_remaining: Remaining depth before cutoff
        :param time_remaining: Remaining time before cutoff
        :return: tuple with maximized value and move
        """
        if game.is_terminal(state, depth_remaining > 0, time_remaining > 0):
            return game.eval(state), None
        best_value = -inf
        best_move = None
        for action in game.actions(state):
            state_after_action = game.result(state, action)
            value, move = self._min_value(game, state_after_action,
                                          depth_remaining-1, time_remaining)
            if value > best_value:
                best_value = value
                best_move = action
        return best_value, best_move

    def _min_value(self, game, state, depth_remaining, time_remaining):
        """ Method returns a minimizing value in the state tree, limited either
            by a terminal state or by reaching another cutoff limit

        :param game: The game, dictate game rules
        :param state: The current game state
        :param depth_remaining: Remaining depth before cutoff
        :param time_remaining: Remaining time before cutoff
        :return: tuple with minimized value and move
        """
        if game.is_terminal(state, depth_remaining > 0, time_remaining > 0):
            return game.eval(state), None
        best_value = inf
        best_move = None
        for action in game.actions(state):
            state_after_action = game.result(state, action)
            value, move = self._max_value(game, state_after_action,
                                          depth_remaining-1, time_remaining)
            if value < best_value:
                best_value = value
                best_move = action
        return best_value, best_move

    def search(self, game, state, depth_remaining=inf, time_remaining=inf):
        """ Overrides Search.search """
        return self._max_value(game, state, depth_remaining, time_remaining)
