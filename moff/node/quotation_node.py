
from .template import CollectionNode

class QuotationNode (CollectionNode):
  
  def __init__ (self, cite=None, nodes=list()):
    super().__init__(nodes)
    self.cite = cite
  
  def write_attributes (self, stream):
    if self.cite:
      stream.write(" cite=\"%s\"" % (str(self.cite),))
  
  # override
  def write (self, stream):
    stream.write("<blockquote")
    self.write_attributes(stream)
    stream.write(">")
    super().write(stream)
    stream.write("</blockquote>")
  