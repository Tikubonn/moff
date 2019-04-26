
from .template import CollectionNode

class EmphasisNode (CollectionNode):
  
  # override
  def write (self, stream):
    stream.write("<em>")
    super().write(stream)
    stream.write("</em>")
  