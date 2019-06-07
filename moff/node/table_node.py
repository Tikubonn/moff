
from .template import CollectionNode


class TableNode (CollectionNode):

    # override
    def write(self, stream):
        stream.write("<table>")
        super().write(stream)
        stream.write("</table>")
