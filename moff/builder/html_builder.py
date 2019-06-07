
from .template import CollectionBuilder
from moff.node import CollectionNode, node


class HTMLBuilder (CollectionBuilder):

    # override
    def build_node(self):
        cnode = CollectionNode()
        for anyone in self.get_collection():
            cnode.add_node(node(anyone))
        return cnode
