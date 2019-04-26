
from .template import Node
from moff.util import sanitize

class InlineCodeNode (Node):
  
  def __init__ (self, code):
    self.code = code
  
  # override
  def write (self, stream):
    stream.write("<code>")
    stream.write(
      sanitize(str(self.code)))
    stream.write("</code>")
  