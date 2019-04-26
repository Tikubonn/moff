
from .template import Builder
from moff.node import AudioNode, SourceNode, ParagraphNode, LinkNode, TextNode
from moff.mimetypes import audio_mimetypes

class AudioSource:
  
  def __init__ (self, src, type=None):
    self.src = src
    self.type = type
  
  def get_src (self):
    return self.src
  
  def get_type (self):
    if self.type:
      return self.type
    src = self.get_src()
    mime, encoding = audio_mimetypes.guess_type(src)
    return mime
  
  def build_source_node (self):
    return SourceNode(
      src = self.get_src(),
      type = self.get_type())
  
class AudioBuilder (Builder):
  
  def __init__ (self, sources=list()):
    self.sources = list(sources)
  
  def add_source (self, source):
    self.sources.append(source)
  
  # override
  def add (self, anyone):
    raise Exception(".add() is unsupported.")
    
  # override
  def is_mergeable (self, builder):
    return False
  
  # override
  def merge (self, builder):
    raise Exception(".merge() is unsupported.")

  def build_alternative_node (self):
    if len(self.sources) == 0:
      raise Exception()
    else:
      source = self.sources[0]
      return ParagraphNode(nodes = [
        TextNode("Your browser has not supported playing audio with HTML5."),
        TextNode("You can download audio from "),
        LinkNode(
          href = source.get_src(),
          target = "_blank",
          nodes = [
            TextNode("here")
          ]),
        TextNode(".")
      ])
  
  # override
  def build_node (self):
    if len(self.sources) == 0:
      raise Exception()
    elif len(self.sources) == 1:
      source = self.sources[0]
      anode = AudioNode(
        src = source.get_src(),
        preload = "none",
        controls = True)
      anode.add_node(
        self.build_alternative_node())
      return anode
    else:
      anode = AudioNode(
        preload = "none",
        controls = True)
      for source in self.sources:
        anode.add_node(
          source.build_source_node())
      anode.add_node(
        self.build_alternative_node())
      return anode
