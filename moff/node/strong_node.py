
from .template import CollectionNode

class StrongNode (CollectionNode):
  
  # override
  def write (self, stream):
    stream.write("<strong>")
    super().write(stream)
    stream.write("</strong>")
  