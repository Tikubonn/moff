
from unittest import TestCase
from moff.parser import Parser
from moff.node import TextNode, StrongNode, ParagraphNode

class TestReadStrong (TestCase):
  
  def test_parse1 (self):
    parser = Parser()
    node1 = parser.parse_string("**strong**")
    node2 = ParagraphNode(nodes=[
      StrongNode(nodes=[
        TextNode("strong")
      ])
    ])
    self.assertEqual(str(node1), str(node2))
  
  def test_parse2 (self):
    parser = Parser()
    node1 = parser.parse_string("**\*strong\***")
    node2 = ParagraphNode(nodes=[
      StrongNode(nodes=[
        TextNode("*strong*")
      ])
    ])
    self.assertEqual(str(node1), str(node2))
  
  def test_parse3 (self):
    parser = Parser()
    node1 = parser.parse_string("text then **strong**!")
    node2 = ParagraphNode(nodes=[
      TextNode("text then "),
      StrongNode(nodes=[
        TextNode("strong")
      ]),
      TextNode("!")
    ])
    self.assertEqual(str(node1), str(node2))
