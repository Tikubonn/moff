
from .template import Node
from moff.util import sanitize

class TextNode (Node):
  
  def __init__ (self, text):
    super().__init__()
    self.text = text
  
  # override
  def write (self, stream):
    stream.write(
      sanitize(str(self.text)))
