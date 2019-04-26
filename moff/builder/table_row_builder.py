
from .template import Builder
from .table_cell_builder import TableCellBuilder
from moff.node import TableRowNode, NodeConvertible

class TableRowBuilder (Builder):
  
  def __init__ (self):
    self.cells = list()
    self.cells.append(self.make_table_cell_builder())
  
  def make_table_cell_builder (self):
    return TableCellBuilder()
  
  def focus_next_cell (self):
    self.cells.append(self.make_table_cell_builder())
  
  # override
  def add (self, node):
    if not isinstance(node, NodeConvertible):
      raise Exception("%s is not %s instance." % (node, NodeConvertible.__name__))
    focused = self.cells[-1]
    focused.add(node)
  
  # override
  def is_mergeable (self, builder):
    return False 
  
  # override
  def merge (self, builder):
    raise Exception(".merge() is unsupported.")
  
  # override
  def build_node (self):
    raise Exception(".build_node() is unsupported.")

  def get_header_node (self):
    rnode = TableRowNode()
    for bu in self.cells[:-1]:
      rnode.add_node(
        bu.get_header_node())
    return rnode
  
  def get_data_node (self):
    rnode = TableRowNode()
    for bu in self.cells[:-1]:
      rnode.add_node(
        bu.get_data_node())
    return rnode
  