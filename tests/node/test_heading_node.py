
from unittest import TestCase
from moff.node import HeadingNode, TextNode
from io import StringIO


class TestHeadingNode (TestCase):

    def test_write(self):
        hnode = HeadingNode(1)
        hnode.add_node(TextNode("moco"))
        hnode.add_node(TextNode("chibi"))
        hnode.add_node(TextNode("nanashi"))
        with StringIO() as stream:
            hnode.write(stream)
            self.assertEqual(
                stream.getvalue(),
                "<h1>mocochibinanashi</h1>")
