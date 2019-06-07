
from .builder import Builder
from moff.node import NodeConvertible
from abc import abstractmethod
import copy


class TreeRootBuilder (Builder):

    def __init__(self, builder):
        self.builder = builder

    def get_builder(self):
        return self.builder

    # private
    def make_tree_root_builder(self, builder):
        return type(self)(builder)

    # override
    def add(self, anyone):
        return self.get_builder().add(anyone)

    # override
    def is_mergeable(self, builder):
        bu = builder
        if isinstance(builder, TreeRootBuilder):
            bu = builder.get_builder()
        return self.get_builder().is_mergeable(bu)

    # override
    def merge(self, builder):
        bu = builder
        if isinstance(builder, TreeRootBuilder):
            bu = builder.get_builder()
        merged = self.get_builder().merge(bu)
        return self.make_tree_root_builder(merged)

    # override
    def build_node(self):
        return self.get_builder().get_root().build_node()


class TreeBuilder (Builder):

    def __init__(self, indentation, parent=None):
        self.collection = [self.make_tree_element()]
        self.indentation = indentation
        self.parent = parent

    @abstractmethod
    def make_tree_element(self):
        pass

    def add_collection(self, anyone):  # add manually
        self.collection.append(anyone)

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def get_collection(self):
        return copy.copy(self.collection)

    def get_indentation(self):
        return self.indentation

    def get_near(self, builder):
        bu = self
        while bu:
            if bu.get_indentation() <= builder.get_indentation():
                return bu
            bu = bu.get_parent()
        raise Error()

    def get_root(self):
        builder = self
        while builder.get_parent():
            builder = builder.get_parent()
        return builder

    # override
    def add(self, anyone):
        if not isinstance(anyone, NodeConvertible):
            raise Exception("%s is not %s instance." %
                            (anyone, NodeConvertible.__name__))
        focused = self.collection[-1]
        focused.add(anyone)

    # override
    def is_mergeable(self, builder):
        return isinstance(builder, TreeBuilder)

    # private
    def merge_builder(self, builder):
        for bu in builder.collection:
            self.add_collection(bu)
        return self

    # private
    def nest_builder(self, builder):
        builder.set_parent(self)
        self.add_collection(builder)
        return builder

    # private
    def exit_builder(self, builder):
        near = self.get_near(builder)
        merged = near.merge(builder)
        return merged

    # override
    def merge(self, builder):
        if isinstance(builder, type(self)):
            if self.get_indentation() == builder.get_indentation():
                return self.merge_builder(builder)
            elif self.get_indentation() < builder.get_indentation():
                return self.nest_builder(builder)
            elif self.get_indentation() > builder.get_indentation():
                return self.exit_builder(builder)
        elif isinstance(builder, TreeBuilder):
            if self.get_indentation() < builder.get_indentation():
                return self.nest_builder(builder)
            elif self.get_indentation() > builder.get_indentation():
                return self.exit_builder(builder)
            else:
                raise TypeError("%s is not %s instance." %
                                (builder, type(self).__name__))
        else:
            raise TypeError("%s is not %s instance." %
                            (builder, TreeBuilder.__name__))
