
from .template import CollectionBuilder
from moff.node import CollectionNode, Node, node

class ListBuilderItem (CollectionBuilder):
  
  # override
  def is_mergeable (self, builder):
    return False
  
  # override
  def merge (self, builder):
    raise Error(".merge() is unsupported.")
  
  # override
  def build_node (self):
    cnode = CollectionNode()
    for anyone in self.get_collection():
      cnode.add_node(node(anyone))
    return cnode
  