
from .template import Builder
from .table_row_builder import TableRowBuilder
from moff.node import TableNode, TableRowNode, TableHeaderNode, TableBodyNode, TableHeaderCellNode, TableDataCellNode, TableSeparatorNode, NodeConvertible

class TableBuilder (Builder):
  
  def __init__ (self):
    self.rows = list()
    self.rows.append(self.make_table_row_builder())
  
  def make_table_row_builder (self):
    return TableRowBuilder()
  
  # override
  def add (self, node):
    if isinstance(node, NodeConvertible):
      if isinstance(node, TableSeparatorNode):
        focused = self.rows[-1]
        focused.focus_next_cell()
      else:
        focused = self.rows[-1]
        focused.add(node)
    else:
      raise Exception("%s is not %s instance." % (node, NodeConvertible.__name__))
  
  # override
  def is_mergeable (self, builder):
    return isinstance(builder, TableBuilder)
  
  # override
  def merge (self, builder):
    for row in builder.rows:
      self.rows.append(row)
    return self
  
  # override
  def build_node (self):
    tnode = TableNode()
    # header
    hnode = TableHeaderNode()
    first = self.rows[0]
    hnode.add_node(first.get_header_node())
    tnode.add_node(hnode)
    # data
    bnode = TableBodyNode()
    for bu in self.rows[1:]:
      bnode.add_node(bu.get_data_node())
    tnode.add_node(bnode)
    # return
    return tnode
  