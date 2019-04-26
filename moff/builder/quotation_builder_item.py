
from .template import CollectionBuilder
from moff.node import CollectionNode

class QuotationBuilderItem (CollectionBuilder):
  
  # override
  def build_node (self):
    cnode = CollectionNode()
    for node in self.get_collection():
      cnode.add_node(node)
    return cnode.trim()
  