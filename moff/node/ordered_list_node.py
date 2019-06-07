
from .template import CollectionNode


class OrderedListNode (CollectionNode):

    # override
    def write(self, stream):
        stream.write("<ol>")
        super().write(stream)
        stream.write("</ol>")
