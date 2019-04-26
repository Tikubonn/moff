
from unittest import TestCase
from moff.parser import Parser
from moff.node import TextNode, LinkNode, ParagraphNode

class TestReadURL (TestCase):
  
  def test_parse (self):
    parser = Parser()
    node1 = parser.parse_string("https://example.com")
    node2 = ParagraphNode(nodes=[
      LinkNode(
        href = "https://example.com",
        target = "_blank",
        nodes = [
          TextNode("https://example.com")
        ])
    ])
    self.assertEqual(str(node1), str(node2))
