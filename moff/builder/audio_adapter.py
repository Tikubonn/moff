
from .template import Adapter
from .audio_builder import AudioBuilder

class AudioAdapter (Adapter):
  
  # override
  def is_mergeable (self, builder):
    return isinstance(builder, AudioBuilder)

class AudioSourceAdapter (AudioAdapter):
  
  def __init__ (self, source):
    self.source = source
  
  # override
  def merge (self, builder):
    builder.add_source(self.source)
    return builder
