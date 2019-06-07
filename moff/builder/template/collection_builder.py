
from .builder import Builder
from moff.node import NodeConvertible
import copy


class CollectionBuilder (Builder):

    def __init__(self):
        self.__collection = list()

    def get_collection(self):
        return copy.copy(self.__collection)

    # override
    def add(self, anyone):
        if not isinstance(anyone, NodeConvertible):
            raise Exception("%s is not %s instance." %
                            (anyone, NodeConvertible.__name__))
        self.__collection.append(anyone)

    # override
    def is_mergeable(self, builder):
        return isinstance(builder, Builder)

    # override
    def merge(self, builder):
        for node in builder.get_collection():
            self.add(node)
        return self
