
from .template import CollectionNode

class TableBodyNode (CollectionNode):
  
  # override
  def write (self, stream):
    stream.write("<tbody>")
    super().write(stream)
    stream.write("</tbody>")
