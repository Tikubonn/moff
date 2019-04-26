
from unittest import TestCase
from moff.parser import Parser
from moff.node import TextNode, EmphasisNode, ParagraphNode

class TestReadEmphasis (TestCase):
  
  def test_parse1 (self):
    parser = Parser()
    node1 = parser.parse_string("*emphasis*")
    node2 = ParagraphNode(nodes=[
      EmphasisNode(nodes=[
        TextNode("emphasis")
      ])
    ])
    self.assertEqual(str(node1), str(node2))
  
  def test_parse2 (self):
    parser = Parser()
    node1 = parser.parse_string("*\*emphasis\**")
    node2 = ParagraphNode(nodes=[
      EmphasisNode(nodes=[
        TextNode("*emphasis*")
      ])
    ])
    self.assertEqual(str(node1), str(node2))
  
  def test_parse3 (self):
    parser = Parser()
    node1 = parser.parse_string("text then *emphasis*!")
    node2 = ParagraphNode(nodes=[
      TextNode("text then "),
      EmphasisNode(nodes=[
        TextNode("emphasis")
      ]),
      TextNode("!")
    ])
    self.assertEqual(str(node1), str(node2))
  