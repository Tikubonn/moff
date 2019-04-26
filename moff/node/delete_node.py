
from .template import CollectionNode

class DeleteNode (CollectionNode):
  
  # override
  def write (self, stream):
    stream.write("<del>")
    super().write(stream)
    stream.write("</del>")
