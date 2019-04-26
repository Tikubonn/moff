
from .template import Node
from moff.attribute import SrcsetAttribute, SizesAttribute

class ImageNode (Node):
  
  def __init__ (
    self, 
    src,
    alt = None,
    title = None,
    width = None,
    height = None,
    crossorigin = None,
    decoding = None,
    importance = None,
    intrinsicsize = None,
    ismap = None,
    referrerpolicy = None,
    usemap = None,
    srcset = None,
    sizes = None):
    self.src = src
    self.alt = alt
    self.title = title
    self.width = width
    self.height = height
    self.crossorigin = crossorigin
    self.decoding = decoding
    self.importance = importance
    self.intrinsicsize = intrinsicsize
    self.ismap = ismap
    self.referrerpolicy = referrerpolicy
    self.usemap = usemap
    self.srcset = srcset if srcset else SrcsetAttribute()
    self.sizes = sizes if sizes else SizesAttribute()
  
  def set_srcset (self, srcset): # SrcsetCollection
    self.srcset = srcset
  
  def set_sizes (self, sizes): # SizesCollection
    self.sizes = sizes
  
  def add_srcset (self, srcset): # Srcset
    self.srcset.add(srcset)
  
  def add_sizes (self, sizes): # Sizes
    self.sizes.add(sizes)
  
  def write_attributes (self, stream):
    if self.src is not None:
      stream.write(" src=\"%s\"" % (str(self.src),))
    if self.alt is not None:
      stream.write(" alt=\"%s\"" % (str(self.alt),))
    if self.title is not None:
      stream.write(" title=\"%s\"" % (str(self.title),))
    if self.width is not None:
      stream.write(" width=\"%s\"" % (str(self.width),))
    if self.height is not None:
      stream.write(" height=\"%s\"" % (str(self.height),))
    if self.crossorigin is not None:
      stream.write(" crossorigin=\"%s\"" % (str(self.crossorigin),))
    if self.decoding is not None:
      stream.write(" decoding=\"%s\"" % (str(self.decoding),))
    if self.importance is not None:
      stream.write(" importance=\"%s\"" % (str(self.importance),))
    if self.intrinsicsize is not None:
      stream.write(" intrinsicsize=\"%s\"" % (str(self.intrinsicsize),))
    if self.ismap is not None:
      stream.write(" ismap=\"%s\"" % (str(self.ismap),))
    if self.referrerpolicy is not None:
      stream.write(" referrerpolicy=\"%s\"" % (str(self.referrerpolicy),))
    if self.usemap is not None:
      stream.write(" usemap=\"%s\"" % (str(self.usemap),))
    self.srcset.write(stream)
    self.sizes.write(stream)
  
  # override
  def write (self, stream):
    stream.write("<img")
    self.write_attributes(stream)
    stream.write(">")
  