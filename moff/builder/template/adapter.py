
from .builder import Builder

class Adapter (Builder):
  
  # override
  def add (self, node):
    raise Exception(".add() is unsupported.")
  
  # override
  def build_node (self):
    raise Exception(".build_node() is unsupported.")
  