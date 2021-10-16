

class _GameMeta(type):
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return ((hasattr(subclass, 'is_terminal')) and callable(subclass.is_terminal)) and \
               ((hasattr(subclass, 'result')) and callable(subclass.result)) and \
               ((hasattr(subclass, 'actions')) and callable(subclass.actions))


class Game(metaclass=_GameMeta):
    def is_terminal(self, state, has_depth, has_time) -> bool:
        pass

    def result(self, state, action):
        pass

    def actions(self, state) -> []:
        pass

    def eval(self, state) -> float:
        pass

    def debug_display(self, state) -> str:
        pass



