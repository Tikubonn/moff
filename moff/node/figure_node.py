
from .template import CollectionNode


class FigureNode (CollectionNode):

    # override
    def write(self, stream):
        stream.write("<figure>")
        super().write(stream)
        stream.write("</figure>")
