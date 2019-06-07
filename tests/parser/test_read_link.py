
from unittest import TestCase
from moff.parser import Parser
from moff.node import LinkNode, TextNode, ParagraphNode


class TestReadLink (TestCase):

    def test_parse1(self):
        parser = Parser()
        node1 = parser.parse_string("[https://example.com]")
        node2 = ParagraphNode(nodes=[
            LinkNode(
                href="https://example.com",
                target="_blank",
                nodes=[
                    TextNode("https://example.com")
                ])
        ])
        self.assertEqual(str(node1), str(node2))

    def test_parse2(self):
        parser = Parser()
        node1 = parser.parse_string("[example.com](https://example.com)")
        node2 = ParagraphNode(nodes=[
            LinkNode(
                href="https://example.com",
                target="_blank",
                nodes=[
                    TextNode("example.com")
                ])
        ])
        self.assertEqual(str(node1), str(node2))

    def test_parse3(self):
        parser = Parser()
        node1 = parser.parse_string("[goto hash](#hash)")
        node2 = ParagraphNode(nodes=[
            LinkNode(
                href="#hash",
                nodes=[
                    TextNode("goto hash")
                ])
        ])
        self.assertEqual(str(node1), str(node2))
