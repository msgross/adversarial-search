"""
Provides an interface for adversarial searches. Implementing classes
will provide an algorithm for searching through some state graph for
a score and suggested move to make through the graph
"""
from math import inf


class _SearchMeta(type):
    """ Metadata for the search type """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'search')) and callable(subclass.search)


class Search(metaclass=_SearchMeta):
    """ Interface for Search algorithms """
    def search(self, state, is_terminal_fn, state_result_fn, actions_fn, eval_fn,
               depth_remaining=inf, time_remaining=inf):
        """ Method returns a search result indicating a recommended move
            and associated score

        :param is_terminal_fn: a function that returns true when a termination condition
                                is fulfilled
        :param state_result_fn: a function that returns the next state given an action
        :param actions_fn: a function that returns available actions given a state
        :param eval_fn: a function that returns an evaluation score on a given state
        :param state: the current state of the game
        :param depth_remaining: the tree depth remaining to continue searching,
                                if it hits 0, search should just return the best result
        :param time_remaining: the remaining time to continue searching,
                                if the time hits 0, search should just return the best result
        :return: a tuple of score, move to make
        """
