
from moff.unit import Width, Resolution
import mimetypes

class Srcset:
  
  def __init__ (self, src, width=None):
    self.src = src
    self.width = width
  
  def get_src (self):
    return self.src
  
  def get_width (self):
    return self.width

  def write (self, stream):
    stream.write(str(self.src))
    if self.width:
      stream.write(" ")
      self.width.write(stream)
  
  def can_be_image_node (self):
    if self.width:
      return isinstance(self.width, Resolution)
    return True
  
class SrcsetAttribute:
  
  def __init__ (self, srcsets=list()):
    self.srcsets = list(srcsets)
  
  def __len__ (self):
    return len(self.srcsets)
  
  def __iter__ (self):
    return iter(self.srcsets)
  
  def add (self, srcset):
    if not isinstance(srcset, Srcset):
      raise Exception("%s is not %s instance." % (srcset, Srcset.__name__))
    self.srcsets.append(srcset)
  
  def write (self, stream):
    if self.srcsets:
      stream.write(" srcset=\"")
      for index, srcset in enumerate(self.srcsets):
        if 0 < index:
          stream.write(", ")
        srcset.write(stream)
      stream.write("\"")

  def can_be_image_node (self):
    for srcset in self.srcsets:
      if not srcset.can_be_image_node():
        return False
    return True
  
