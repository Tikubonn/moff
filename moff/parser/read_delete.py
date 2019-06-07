
from moff.node import DeleteNode, TextNode
from moff.util import read_until_string

#
# ~~ ... ~~
#


def read_delete(preread, stream, parser, options):
    read1 = read_until_string(stream, "~~", use_escape=True)
    stream.get()
    stream.get()
    dnode = DeleteNode()
    dnode.add_node(TextNode(read1))
    return dnode
