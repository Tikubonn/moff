
from unittest import TestCase
from moff.node import ParagraphNode, TextNode
from io import StringIO

class TestParagraphNode (TestCase):
  
  def test_write (self):
    pnode = ParagraphNode()
    pnode.add_node(TextNode("moco"))
    pnode.add_node(TextNode("chibi"))
    pnode.add_node(TextNode("nisechibi"))
    with StringIO() as stream:
      pnode.write(stream)
      self.assertEqual(
        stream.getvalue(),
        "<p>mocochibinisechibi</p>")
