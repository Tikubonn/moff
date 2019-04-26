
from .template import CollectionNode

class UnOrderedListNode (CollectionNode):
  
  # override
  def write (self, stream):
    stream.write("<ul>")
    super().write(stream)
    stream.write("</ul>")
  