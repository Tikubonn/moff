
from .template import CollectionNode

class ListItemNode (CollectionNode):
  
  # override
  def write (self, stream):
    stream.write("<li>")
    super().write(stream)
    stream.write("</li>")
  