
from .template import CollectionNode

class LinkNode (CollectionNode):
  
  def __init__ (
    self,
    href=None,
    hreflang=None,
    download=None,
    ping=None,
    referrerpolicy=None,
    rel=None,
    target=None,
    type=None,
    id=None,
    nodes=list()):
    super().__init__(nodes)
    self.href = href
    self.hreflang = hreflang
    self.download = download
    self.ping = ping
    self.referrerpolicy = referrerpolicy
    self.rel = rel
    self.target = target
    self.type = type
    self.id = id
  
  def write_attributes (self, stream):
    if self.href is not None:
      stream.write(" href=\"%s\"" % (str(self.href),))
    if self.hreflang is not None:
      stream.write(" hreflang=\"%s\"" % (str(self.hreflang),))
    if self.download is not None:
      if self.download is True:
        stream.write(" download")
      else:
        stream.write(" download=\"%s\"" % (str(self.download),))
    if self.ping is not None:
      stream.write(" ping=\"%s\"" % (str(self.ping),))
    if self.referrerpolicy is not None:
      stream.write(" referrerpolicy=\"%s\"" % (str(self.referrerpolicy),))
    if self.rel is not None:
      stream.write(" rel=\"%s\"" % (str(self.rel),))
    if self.target is not None:
      stream.write(" target=\"%s\"" % (str(self.target),))
    if self.type is not None:
      stream.write(" type=\"%s\"" % (str(self.type),))
    if self.id is not None:
      stream.write(" id=\"%s\"" % (str(self.id),))
  
  # override
  def write (self, stream):
    stream.write("<a")
    self.write_attributes(stream)
    stream.write(">")
    super().write(stream)
    stream.write("</a>")
  