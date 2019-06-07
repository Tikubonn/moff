
from .template import CollectionBuilder
from moff.node import HeadingNode, node


class HeadingBuilder (CollectionBuilder):

    def __init__(self, hnum):
        super().__init__()
        self.hnum = hnum

    # override
    def is_mergeable(self, builder):
        return (
            super().is_mergeable(builder) and
            isinstance(builder, HeadingBuilder) and
            self.hnum == builder.hnum)

    # override
    def build_node(self):
        hnode = HeadingNode(self.hnum)
        for anyone in self.get_collection():
            hnode.add_node(node(anyone))
        return hnode
