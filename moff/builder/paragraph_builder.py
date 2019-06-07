
from .template import CollectionBuilder
from moff.node import ParagraphNode, node


class ParagraphBuilder (CollectionBuilder):

    # override
    def is_mergeable(self, builder):
        return isinstance(builder, ParagraphBuilder)

    # override
    def build_node(self):
        pnode = ParagraphNode()
        for anyone in self.get_collection():
            pnode.add_node(node(anyone))
        return pnode.trim()
