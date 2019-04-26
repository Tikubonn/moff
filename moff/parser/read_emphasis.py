
from moff.node import EmphasisNode, TextNode
from moff.util import read_until

#
# * ... * 
#

def read_emphasis (preread, stream, parser, options):
  read = read_until(stream, "*", use_escape=True)
  stream.get()
  enode = EmphasisNode()
  enode.add_node(TextNode(read))
  return enode
