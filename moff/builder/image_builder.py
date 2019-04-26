
from .template import Builder
from moff.node import LinkNode, PictureNode, SourceNode, ImageNode
from moff.attribute import SrcsetAttribute, SizesAttribute
from moff.mimetypes import image_mimetypes

def get_type (src):
  mime, encoding = image_mimetypes.guess_type(src)
  return mime

class ImageCase:
  
  def __init__ (self, srcset=None, sizes=None, media=None, type=None):
    self.srcset = srcset if srcset else SrcsetAttribute() 
    self.sizes = sizes if sizes else SizesAttribute()
    self.media = media
    self.type = type
  
  def add_srcset (self, srcset):
    self.srcset.add(srcset)
  
  def add_sizes (self, sizes):
    self.sizes.add(sizes)
  
  def set_media (self, media):
    self.media = media
  
  def set_type (self, type):
    self.type = type
  
  def get_srcset (self):
    return self.srcset
  
  def get_sizes (self):
    return self.sizes
  
  def get_media (self):
    return self.media
  
  def guess_type (self):
    typeset = set([ get_type(srcset.get_src()) for srcset in self.srcset ])
    if len(typeset) == 1:
      type, = typeset
      return type
    return None 
  
  def get_type (self):
    if self.type:
      return self.type
    return self.guess_type()
  
  def build_source_node (self):
    return SourceNode(
      srcset = self.get_srcset(),
      sizes = self.get_sizes(),
      media = self.get_media(),
      type = self.get_type())
  
  def can_be_image_node (self):
    if self.media:
      return False
    if self.type:
      return False
    return self.srcset.can_be_image_node()
  
  def apply_to_image_node (self, image):
    image.set_srcset(self.srcset)
    image.set_sizes(self.sizes)
  
class ImageCaseCollection:
  
  def __init__ (self):
    self.cases = list()
  
  def next_case (self):
    case = ImageCase()
    self.cases.append(case)
  
  def add_srcset (self, srcset):
    if not self.cases:
      self.next_case()
    case = self.cases[-1]
    case.add_srcset(srcset)
  
  def add_sizes (self, sizes):
    if not self.cases:
      self.next_case()
    case = self.cases[-1]
    case.add_sizes(sizes)
  
  def set_media (self, media):
    if not self.cases:
      self.next_case()
    case = self.cases[-1]
    case.set_media(media)
  
  def set_type (self, type):
    if not self.cases:
      self.next_case()
    case = self.cases[-1]
    case.set_type(type)
  
  def can_be_image_node (self):
    if len(self.cases) == 0:
      return True
    if len(self.cases) == 1:
      case = self.cases[0]
      return case.can_be_image_node()
    return False
  
  def apply_to_image_node (self, image):
    if self.cases:
      case = self.cases[0]
      case.apply_to_image_node(image)
  
  def apply_to_picture_node (self, picture):
    for case in self.cases:
      snode = case.build_source_node()
      picture.add_node(snode)

class ImageBuilder (Builder):
  
  def __init__ (self, src, alt=None, title=None, link=None):
    self.src = src
    self.alt = alt
    self.title = title
    self.link = link
    self.cases = ImageCaseCollection()
  
  def add_alt (self, alt):
    if not self.alt:
      self.alt = alt
    else:
      self.alt += alt
  
  def add_title (self, title):
    if not self.title:
      self.title = title
    else:
      self.title += title
  
  def set_link (self, link):
    self.link = link
  
  def next_case (self):
    self.cases.next_case()
  
  def add_srcset (self, srcset):
    self.cases.add_srcset(srcset)
  
  def add_sizes (self, sizes):
    self.cases.add_sizes(sizes)
  
  def set_media (self, media):
    self.cases.set_media(media)
  
  def set_type (self, type):
    self.cases.set_type(type)
  
  # override
  def add (self, builder):
    raise Exception(".add() is unsupported.")
  
  # override
  def is_mergeable (self, builder):
    return False
  
  # override
  def merge (self, builder):
    raise Exception(".merge() is unsupported.")
  
  def build_image_node (self):
    inode = ImageNode(
      src = self.src,
      alt = self.alt,
      title = self.title,
      decoding = "async")
    self.cases.apply_to_image_node(inode)
    return inode
  
  def build_picture_node (self):
    pnode = PictureNode()
    self.cases.apply_to_picture_node(pnode)
    inode = ImageNode(
      src = self.src,
      alt = self.alt,
      title = self.title,
      decoding = "async")
    pnode.add_node(inode)
    return pnode 
  
  # override
  def build_node (self):
    node = None 
    if self.cases.can_be_image_node():
      node = self.build_image_node()
    else:
      node = self.build_picture_node()
    lnode = LinkNode(
      href = self.link or self.src, 
      target = "_blank")
    lnode.add_node(node)
    return lnode
