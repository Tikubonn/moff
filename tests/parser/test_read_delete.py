
from unittest import TestCase
from moff.parser import Parser
from moff.node import TextNode, DeleteNode, ParagraphNode


class TestReadDelete (TestCase):

    def test_parse1(self):
        parser = Parser()
        node1 = parser.parse_string("~~delete~~")
        node2 = ParagraphNode(nodes=[
            DeleteNode(nodes=[
                TextNode("delete")
            ])
        ])
        self.assertEqual(str(node1), str(node2))

    def test_parse2(self):
        parser = Parser()
        node1 = parser.parse_string("~~\~delete\~~~")
        node2 = ParagraphNode(nodes=[
            DeleteNode(nodes=[
                TextNode("~delete~")
            ])
        ])
        self.assertEqual(str(node1), str(node2))

    def test_parse3(self):
        parser = Parser()
        node1 = parser.parse_string("text then ~~delete~~!")
        node2 = ParagraphNode(nodes=[
            TextNode("text then "),
            DeleteNode(nodes=[
                TextNode("delete")
            ]),
            TextNode("!")
        ])
        self.assertEqual(str(node1), str(node2))
