
from unittest import TestCase
from moff.parser import Parser
from moff.node import InlineCodeNode, TextNode, ParagraphNode
from io import StringIO

class TestReadInlineCode (TestCase):
  
  def test_parse1 (self):
    parser = Parser()
    node1 = parser.parse_string("`<b>example</b>`")
    node2 = ParagraphNode(nodes=[
      InlineCodeNode("<b>example</b>")
    ])
    self.assertEqual(str(node1), str(node2))
  
  def test_parse2 (self):
    parser = Parser()
    node1 = parser.parse_string("text then `<b>example</b>`!")
    node2 = ParagraphNode(nodes=[
      TextNode("text then "),
      InlineCodeNode("<b>example</b>"),
      TextNode("!")
    ])
    self.assertEqual(str(node1), str(node2))
  