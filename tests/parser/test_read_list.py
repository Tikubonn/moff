
from unittest import TestCase
from moff.parser import Parser
from moff.node import TextNode, OrderedListNode, UnOrderedListNode, ListItemNode, EmphasisNode

class TestReadList (TestCase):
  
  def test_parse_ordered_list1 (self):
    parser = Parser()
    node1 = parser.parse_string(
      "- a\n" + 
      "- b\n" + 
      "- c")
    node2 = OrderedListNode(nodes=[
      ListItemNode(nodes=[
        TextNode("a")
      ]),
      ListItemNode(nodes=[
        TextNode("b")
      ]),
      ListItemNode(nodes=[
        TextNode("c")
      ])
    ])
    self.assertEqual(str(node1), str(node2))
  
  def test_parse_unordered_list1 (self):
    parser = Parser()
    node1 = parser.parse_string(
      "* a\n" + 
      "* b\n" + 
      "* c")
    node2 = UnOrderedListNode(nodes=[
      ListItemNode(nodes=[
        TextNode("a")
      ]),
      ListItemNode(nodes=[
        TextNode("b")
      ]),
      ListItemNode(nodes=[
        TextNode("c")
      ])
    ])
    self.assertEqual(str(node1), str(node2))
  
  def test_parse_list1 (self):
    parser = Parser()
    node1 = parser.parse_string(
      "- 0\n" + 
      "  * 1\n" + 
      "    - 2\n" + 
      "  * 1")
    node2 = OrderedListNode(nodes=[
      ListItemNode(nodes=[
        TextNode("0"),
        UnOrderedListNode(nodes=[
          ListItemNode(nodes=[
            TextNode("1"),
            OrderedListNode(nodes=[
              ListItemNode(nodes=[
                TextNode("2")
              ])
            ])
          ]),
          ListItemNode(nodes=[
            TextNode("1")
          ])
        ])
      ])
    ])
    self.assertEqual(str(node1), str(node2))
  
  def test_parse_ordered_list2 (self):
    parser = Parser()
    node1 = parser.parse_string(
      "- *a*\n" + 
      "- *b*\n" + 
      "- *c*")
    node2 = OrderedListNode(nodes=[
      ListItemNode(nodes=[
        EmphasisNode(nodes=[
          TextNode("a")
        ])
      ]),
      ListItemNode(nodes=[
        EmphasisNode(nodes=[
          TextNode("b")
        ])
      ]),
      ListItemNode(nodes=[
        EmphasisNode(nodes=[
          TextNode("c")
        ])
      ])
    ])
    self.assertEqual(str(node1), str(node2))
  
  def test_parse_unordered_list2 (self):
    parser = Parser()
    node1 = parser.parse_string(
      "* *a*\n" + 
      "* *b*\n" + 
      "* *c*")
    node2 = UnOrderedListNode(nodes=[
      ListItemNode(nodes=[
        EmphasisNode(nodes=[
          TextNode("a")
        ])
      ]),
      ListItemNode(nodes=[
        EmphasisNode(nodes=[
          TextNode("b")
        ])
      ]),
      ListItemNode(nodes=[
        EmphasisNode(nodes=[
          TextNode("c")
        ])
      ])
    ])
    self.assertEqual(str(node1), str(node2))
    