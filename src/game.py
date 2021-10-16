

class _GameMeta(type):
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'search')) and callable(subclass.search)


class Game(metaclass=_GameMeta):
    def is_terminal(self, state, has_depth, has_time):
        pass

    def result(self, state, action):
        pass

    def actions(self, state):
        pass

    def eval(self, state):
        pass
