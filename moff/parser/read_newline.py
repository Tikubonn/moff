
from moff.node import NewlineNode, TextNode

def read_newline (preread, stream, parser, options):
  character = stream.peek()
  if character == "\n":
    return NewlineNode()
  else:
    return TextNode(preread)
  