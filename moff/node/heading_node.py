
from .template import CollectionNode

class HeadingNode (CollectionNode):
  
  def __init__ (self, hnum=1, nodes=list()):
    super().__init__(nodes)
    self.hnum = hnum
  
  # override
  def write (self, stream):
    stream.write("<h%d>" % (self.hnum,))
    super().write(stream)
    stream.write("</h%d>" % (self.hnum,))
  