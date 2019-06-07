
from .template import TreeBuilder, TreeRootBuilder
from .quotation_builder_item import QuotationBuilderItem
from moff.node import QuotationNode, node


class QuotationRootBuilder (TreeRootBuilder):

    pass


class QuotationBuilder (TreeBuilder):

    def __init__(self, indentation, parent=None, cite=None):
        super().__init__(indentation, parent=parent)
        self.cite = cite

    def set_cite(self, cite):
        self.cite = cite

    def get_cite(self):
        return self.cite

    # override
    def make_tree_element(self):
        return QuotationBuilderItem()

    # override
    def is_mergeable(self, builder):
        return isinstance(builder, QuotationBuilder)

    # override
    def build_node(self):
        pnode = QuotationNode(cite=self.cite)
        for anyone in self.get_collection():
            pnode.add_node(node(anyone))
        return pnode
