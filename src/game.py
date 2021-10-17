

class _GameMeta(type):
    """ Metadata for the Game class """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return ((hasattr(subclass, 'is_terminal')) and callable(subclass.is_terminal)) and \
               ((hasattr(subclass, 'result')) and callable(subclass.result)) and \
               ((hasattr(subclass, 'actions')) and callable(subclass.actions)) and \
               ((hasattr(subclass, 'eval')) and callable(subclass.eval)) and \
               ((hasattr(subclass, 'debug_display')) and callable(subclass.debug_display))


class Game(metaclass=_GameMeta):
    """ Represents the rules and conditions of a game """
    def is_terminal(self, state, has_depth, has_time) -> bool:
        """ Return true if the game is over, either due to a non-winnable
            condition or a winner is decided

        :param state: the current state of the game
        :param has_depth: True if there is remaining depth available, False otherwise
        :param has_time: True if there is remaining time left, False otherwise
        :return: True if the game is over, False otherwise
        """
        pass

    def result(self, state, action):
        """ Return the next state given an action

        :param state: the current state
        :param action: the action to apply to the state
        :return: updated state with the action applied
        """
        pass

    def actions(self, state) -> []:
        """ Returns a list of valid actions that can be taken given a state

        :param state: the current state
        :return: list of valid actions
        """
        pass

    def eval(self, state) -> float:
        """ Returns a score of a given state

        :param state: The state
        :return: score of the given state
        """
        pass

    def debug_display(self, state) -> str:
        """ Debug display returns a string representation
            of the current state

        :param state: The current state
        :return: string representation of the state
        """
        pass



