
from .template import CollectionBuilder
from moff.node import TableHeaderCellNode, TableDataCellNode


class TableCellBuilder (CollectionBuilder):

    # override
    def is_mergeable(self):
        return False

    # override
    def merge(self, builder):
        raise Error(".merge() is unsupported.")

    # override
    def build_node(self):
        raise Error(".build_node() is unsupported.")

    # override
    def get_header_node(self):
        hnode = TableHeaderCellNode()
        for node in self.get_collection():
            hnode.add_node(node)
        return hnode.trim()

    # override
    def get_data_node(self):
        dnode = TableDataCellNode()
        for node in self.get_collection():
            dnode.add_node(node)
        return dnode.trim()
