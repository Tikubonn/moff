
from unittest import TestCase
from moff.parser import Parser
from moff.node import TextNode, ParagraphNode

class TestReadEscape (TestCase):
  
  def test_parse1 (self):
    parser = Parser()
    node1 = parser.parse_string("\*emphasis\*")
    node2 = ParagraphNode(nodes=[
      TextNode("*emphasis*")
    ])
    self.assertEqual(str(node1), str(node2))
  
  def test_parse2 (self):
    parser = Parser()
    node1 = parser.parse_string("text then \*emphasis\*!")
    node2 = ParagraphNode(nodes=[
      TextNode("text then *emphasis*!")
    ])
    self.assertEqual(str(node1), str(node2))
  
  def test_parse3 (self):
    parser = Parser()
    node1 = parser.parse_string("a\\\nb")
    node2 = ParagraphNode(nodes=[
      TextNode("a\nb")
    ])
    self.assertEqual(str(node1), str(node2))
  