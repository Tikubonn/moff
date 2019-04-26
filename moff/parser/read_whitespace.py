
from moff.node import WhitespaceNode

def read_whitespace (preread, stream, parser, options):
  return WhitespaceNode(preread)
  