
from .template import Node
from moff.util import sanitize


class CodeNode (Node):

    def __init__(self, code, language=None):
        self.code = code
        self.language = language

    # override
    def write(self, stream):
        stream.write("<pre>")
        stream.write("<code>")
        stream.write(
            sanitize(str(self.code)))
        stream.write("</code>")
        stream.write("</pre>")
