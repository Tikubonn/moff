
from .list_builder import ListBuilder, ListRootBuilder
from moff.node import UnOrderedListNode, ListItemNode, node

class UnOrderedListRootBuilder (ListRootBuilder):
  
  pass

class UnOrderedListBuilder (ListBuilder):
  
  # override
  def build_node (self):
    lnode = UnOrderedListNode()
    for anyone in self.get_collection():
      inode = ListItemNode()
      inode.add_node(node(anyone))
      lnode.add_node(inode)
    return lnode
  