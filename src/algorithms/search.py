import math


class _SearchMeta(type):
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'search')) and callable(subclass.search)


class Search(metaclass=_SearchMeta):
    def search(self, game, state, depth=math.inf, time_remaining=math.inf):
        pass
