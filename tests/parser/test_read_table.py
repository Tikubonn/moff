
from unittest import TestCase
from moff.parser import Parser
from moff.node import TextNode, TableNode, TableHeaderNode, TableBodyNode, TableRowNode, TableHeaderCellNode, TableDataCellNode, EmphasisNode


class TestReadTable (TestCase):

    def test_parse1(self):
        parser = Parser()
        node1 = parser.parse_string(
            "| name | age |\n" +
            "| anonymous | unknown |")
        node2 = TableNode(nodes=[
            TableHeaderNode(nodes=[
                TableRowNode(nodes=[
                    TableHeaderCellNode(nodes=[
                        TextNode("name")
                    ]),
                    TableHeaderCellNode(nodes=[
                        TextNode("age")
                    ])
                ])
            ]),
            TableBodyNode(nodes=[
                TableRowNode(nodes=[
                    TableDataCellNode(nodes=[
                        TextNode("anonymous")
                    ]),
                    TableDataCellNode(nodes=[
                        TextNode("unknown")
                    ])
                ])
            ])
        ])
        self.assertEqual(str(node1), str(node2))

    def test_parse2(self):
        parser = Parser()
        node1 = parser.parse_string(
            "| name \| age |\n" +
            "| anonymous \| unknown |")
        node2 = TableNode(nodes=[
            TableHeaderNode(nodes=[
                TableRowNode(nodes=[
                    TableHeaderCellNode(nodes=[
                        TextNode("name | age")
                    ])
                ])
            ]),
            TableBodyNode(nodes=[
                TableRowNode(nodes=[
                    TableDataCellNode(nodes=[
                        TextNode("anonymous | unknown")
                    ])
                ])
            ])
        ])
        self.assertEqual(str(node1), str(node2))

    def test_parse3(self):
        parser = Parser()
        node1 = parser.parse_string(
            "| *name* | *age* |\n" +
            "| *anonymous* | *unknown* |")
        node2 = TableNode(nodes=[
            TableHeaderNode(nodes=[
                TableRowNode(nodes=[
                    TableHeaderCellNode(nodes=[
                        EmphasisNode(nodes=[
                          TextNode("name")
                          ])
                    ]),
                    TableHeaderCellNode(nodes=[
                        EmphasisNode(nodes=[
                            TextNode("age")
                        ])
                    ])
                ])
            ]),
            TableBodyNode(nodes=[
                TableRowNode(nodes=[
                    TableDataCellNode(nodes=[
                        EmphasisNode(nodes=[
                          TextNode("anonymous")
                          ])
                    ]),
                    TableDataCellNode(nodes=[
                        EmphasisNode(nodes=[
                            TextNode("unknown")
                        ])
                    ])
                ])
            ])
        ])
        self.assertEqual(str(node1), str(node2))
