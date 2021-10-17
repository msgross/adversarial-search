import math
from src.game import Game

class _SearchMeta(type):
    """ Metadata for the search type
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'search')) and callable(subclass.search)


class Search(metaclass=_SearchMeta):
    """ Interface for Search algorithms """
    def search(self, game: Game, state, depth=math.inf, time_remaining=math.inf):
        """ Method returns a search result indicating a recommended move
            and associated score

        :param game: a Game that provides insight into rules and heuristics to determine search behavior
        :param state: the current state of the game
        :param depth: the tree depth remaining to continue searching, if it hits 0, search should just
                      return the best result
        :param time_remaining: the remaining time to continue searching, if the time hits 0, search should
                                just return the best result
        :return: a tuple of score, move
        """
        pass
