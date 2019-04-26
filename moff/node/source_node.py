
from .template import Node
from moff.attribute import SrcsetAttribute, SizesAttribute

class SourceNode (Node):
  
  def __init__ (
    self,
    src = None,
    type = None,
    media = None,
    srcset = None,
    sizes = None):
    self.src = src
    self.type = type
    self.media = media
    self.srcset = srcset if srcset else SrcsetAttribute()
    self.sizes = sizes if sizes else SizesAttribute()
  
  def add_srcset (self, srcset):
    self.srcset.add(srcset)
  
  def add_sizes (self, sizes):
    self.sizes.add(sizes)

  def write_attributes (self, stream):
    if not self.src and len(self.srcset) == 0:
      raise Exception(".src or .srcset is necessary.")
    if self.src:
      stream.write(" src=\"%s\"" % (str(self.src),))
    if self.type:
      stream.write(" type=\"%s\"" % (str(self.type),))
    if self.media:
      stream.write(" media=\"%s\"" % (str(self.media),))
    self.srcset.write(stream)
    self.sizes.write(stream)
  
  # override
  def write (self, stream):
    stream.write("<source")
    self.write_attributes(stream)
    stream.write(">")
  