
from .template import CollectionNode


class PictureNode (CollectionNode):

    # override
    def write(self, stream):
        stream.write("<picture>")
        super().write(stream)
        stream.write("</picture>")
