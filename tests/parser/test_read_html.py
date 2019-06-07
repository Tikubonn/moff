
from unittest import TestCase
from moff.parser import Parser
from moff.node import HTMLNode, TextNode, ParagraphNode


class TestReadHTML (TestCase):

    def test_parse1(self):
        parser = Parser()
        node = parser.parse_string("<b>bold</b>")
        self.assertEqual(
            str(node),
            "<b>bold</b>")

    def test_parse2(self):
        parser = Parser()
        node = parser.parse_string("<img src=\"example.png\"/>")
        self.assertEqual(
            str(node),
            "<img src=\"example.png\"/>")

    def test_parse3(self):
        parser = Parser()
        node1 = parser.parse_string("text then <b>bold</b>!")
        node2 = ParagraphNode(nodes=[
            TextNode("text then "),
            HTMLNode("<b>bold</b>"),
            TextNode("!")
        ])
        self.assertEqual(str(node1), str(node2))

    def test_parse4(self):
        parser = Parser()
        node1 = parser.parse_string("text then <img src=\"example.png\"/>!")
        node2 = ParagraphNode(nodes=[
            TextNode("text then "),
            HTMLNode("<img src=\"example.png\"/>"),
            TextNode("!")
        ])
        self.assertEqual(str(node1), str(node2))
