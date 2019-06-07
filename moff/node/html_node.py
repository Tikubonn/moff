
from .template import Node


class HTMLNode (Node):

    def __init__(self, code):
        self.code = code

    # override
    def write(self, stream):
        stream.write(str(self.code))
