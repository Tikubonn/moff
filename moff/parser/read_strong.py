
from moff.node import StrongNode, TextNode
from moff.util import read_until_string

#
# ** ... **
#


def read_strong(preread, stream, parser, options):
    read1 = read_until_string(stream, "**", use_escape=True)
    stream.get()
    stream.get()
    snode = StrongNode()
    snode.add_node(TextNode(read1))
    return snode
