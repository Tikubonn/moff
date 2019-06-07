
from .template import Node


class NewlineNode (Node):

    # override
    def write(self, stream):
        stream.write("<br>")
