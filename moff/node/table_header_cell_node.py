
from .template import CollectionNode


class TableHeaderCellNode (CollectionNode):

    # override
    def write(self, stream):
        stream.write("<th>")
        super().write(stream)
        stream.write("</th>")
