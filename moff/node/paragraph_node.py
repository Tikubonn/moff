
from .template import CollectionNode

class ParagraphNode (CollectionNode):
  
  # override
  def write (self, stream):
    stream.write("<p>")
    super().write(stream)
    stream.write("</p>")
  