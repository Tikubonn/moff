
from unittest import TestCase
from moff.parser import Parser
from moff.node import TextNode, NewlineNode, ParagraphNode

class TestReadNewline (TestCase):
  
  def test_parse1 (self):
    parser = Parser()
    node1 = parser.parse_string("newline  \n")
    node2 = ParagraphNode(nodes=[
      TextNode("newline"),
      NewlineNode()
    ])
    self.assertEqual(str(node1), str(node2))
  