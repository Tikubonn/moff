
from unittest import TestCase
from moff.node import QuotationNode, TextNode
from io import StringIO

class TestQuotationNode (TestCase):
  
  def test_write1 (self):
    qnode = QuotationNode()
    qnode.add_node(TextNode("moco"))
    qnode.add_node(TextNode("chibi"))
    qnode.add_node(TextNode("nanashi"))
    with StringIO() as stream:
      qnode.write(stream)
      self.assertEqual(
        stream.getvalue(),
        "<blockquote>mocochibinanashi</blockquote>")
      
  def test_write2 (self):
    qnode = QuotationNode(cite="https://example.com")
    qnode.add_node(TextNode("moco"))
    qnode.add_node(TextNode("chibi"))
    qnode.add_node(TextNode("nanashi"))
    with StringIO() as stream:
      qnode.write(stream)
      self.assertEqual(
        stream.getvalue(),
        "<blockquote cite=\"https://example.com\">mocochibinanashi</blockquote>")
    