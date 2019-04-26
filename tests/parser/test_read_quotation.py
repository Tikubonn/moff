
from unittest import TestCase
from moff.parser import Parser
from moff.node import TextNode, QuotationNode

class TestReadQuotation (TestCase):
  
  def test_parse1 (self):
    parser = Parser()
    node1 = parser.parse_string("> a\n> b\n> c")
    node2 = QuotationNode(nodes=[
      TextNode("a"),
      TextNode("b"),
      TextNode("c")
    ])
    self.assertEqual(str(node1), str(node2))
  
  def test_parse2 (self):
    parser = Parser()
    node1 = parser.parse_string("> a\n> b\n> c\n>> https://example.com")
    node2 = QuotationNode(
      cite = "https://example.com",
      nodes=[
        TextNode("a"),
        TextNode("b"),
        TextNode("c")
      ])
    self.assertEqual(str(node1), str(node2))
  