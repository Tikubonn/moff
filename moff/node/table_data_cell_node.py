
from .template import CollectionNode


class TableDataCellNode (CollectionNode):

    # override
    def write(self, stream):
        stream.write("<td>")
        super().write(stream)
        stream.write("</td>")
