
from .node import Node
from moff.node.whitespace_node import WhitespaceNode
import copy


class CollectionNode (Node):

    def __init__(self, nodes=list()):
        self.__nodes = list(nodes)

    def add_node(self, node):
        self.__nodes.append(node)

    def get_nodes(self):
        return copy.copy(self.__nodes)

    # override
    def write(self, stream):
        for node in self.get_nodes():
            node.write(stream)

    def trim(self):
        start = None
        for index, node in enumerate(self.__nodes):
            if isinstance(node, WhitespaceNode):
                start = index + 1
            else:
                break
        end = None
        for index, node in reversed(list(enumerate(self.__nodes))):
            if isinstance(node, WhitespaceNode):
                end = index
            else:
                break
        self.__nodes = self.__nodes[start: end]
        return self
