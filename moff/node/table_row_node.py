
from .template import CollectionNode


class TableRowNode (CollectionNode):

    # override
    def write(self, stream):
        stream.write("<tr>")
        super().write(stream)
        stream.write("</tr>")
