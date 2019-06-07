
from .list_builder import ListBuilder, ListRootBuilder
from moff.node import OrderedListNode, ListItemNode, node


class OrderedListRootBuilder (ListRootBuilder):

    pass


class OrderedListBuilder (ListBuilder):

    # override
    def build_node(self):
        lnode = OrderedListNode()
        for anyone in self.get_collection():
            inode = ListItemNode()
            inode.add_node(node(anyone))
            lnode.add_node(inode)
        return lnode
