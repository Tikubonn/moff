
from .node_convertible import NodeConvertible
from abc import abstractmethod
from io import StringIO

class Node (NodeConvertible):
  
  @abstractmethod
  def write (self, stream):
    pass
  
  def __str__ (self):
    with StringIO() as stream:
      self.write(stream)
      return stream.getvalue()
  
  # override
  def __node__ (self):
    return self
