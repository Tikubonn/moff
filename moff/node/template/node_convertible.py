
from abc import ABC, abstractmethod

def node (node):
  if not isinstance(node, NodeConvertible):
    raise TypeError("%s is not %s instance." % (node, NodeConvertible.__name__))
  return node.__node__()

class NodeConvertible (ABC):
  
  @abstractmethod
  def __node__ (self):
    pass
  