
from .template import Node


class TableSeparatorNode (Node):

    # override
    def write(self, stream):
        raise Error(".write() is unsupported.")
