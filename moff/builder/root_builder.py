
from .template import CollectionBuilder
from moff.node import RootNode, node

class RootBuilder (CollectionBuilder):
  
  # override
  def build_node (self):
    rnode = RootNode()
    for anyone in self.get_collection():
      rnode.add_node(node(anyone))
    return rnode
  