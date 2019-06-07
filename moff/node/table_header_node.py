
from .template import CollectionNode


class TableHeaderNode (CollectionNode):

    # override
    def write(self, stream):
        stream.write("<thead>")
        super().write(stream)
        stream.write("</thead>")
