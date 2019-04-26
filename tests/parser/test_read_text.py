
from unittest import TestCase
from moff.parser import Parser
from moff.node import TextNode, ParagraphNode

class TestReadText (TestCase):
  
  def test_parse1 (self):
    parser = Parser()
    node1 = parser.parse_string("example")
    node2 = ParagraphNode(nodes=[
      TextNode("example")
    ])
    self.assertEqual(str(node1), str(node2))
  
  def test_parse2 (self):
    parser = Parser()
    node1 = parser.parse_string("example&example")
    node2 = ParagraphNode(nodes=[
      TextNode("example&example")
    ])
    self.assertEqual(str(node1), str(node2))
    