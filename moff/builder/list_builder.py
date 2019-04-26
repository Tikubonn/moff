
from .template import TreeBuilder, TreeRootBuilder
from .list_builder_item import ListBuilderItem

class ListRootBuilder (TreeRootBuilder):
  
  pass

class ListBuilder (TreeBuilder):
  
  # override
  def make_tree_element (self):
    return ListBuilderItem()
  
  # override
  def nest_builder (self, builder):
    builder.set_parent(self)
    self.add(builder)
    return builder
  