
from unittest import TestCase
from moff.parser import Parser
from moff.node import TextNode, HeadingNode, RootNode


class TestReadHeading (TestCase):

    def test_parse1(self):
        parser = Parser()
        node1 = parser.parse_string("# h1")
        node2 = HeadingNode(1, nodes=[
            TextNode("h1")
        ])
        self.assertEqual(str(node1), str(node2))

    def test_parse2(self):
        parser = Parser()
        node1 = parser.parse_string("# h1\n# h1")
        node2 = HeadingNode(1, nodes=[
            TextNode("h1"),
            TextNode("h1")
        ])
        self.assertEqual(str(node1), str(node2))

    def test_parse3(self):
        parser = Parser()
        node1 = parser.parse_string("# h1\n## h2")
        node2 = RootNode(nodes=[
            HeadingNode(1, nodes=[
                TextNode("h1")
            ]),
            HeadingNode(2, nodes=[
                TextNode("h2")
            ])
        ])
        self.assertEqual(str(node1), str(node2))
