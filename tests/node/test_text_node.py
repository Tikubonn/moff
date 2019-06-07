
from unittest import TestCase
from moff.node import TextNode
from io import StringIO


class TestTextNode (TestCase):

    def write_test1(self):
        node = TextNode("moco chibi nanashi")
        with StringIO() as stream:
            node.write(stream)
            self.assertEqual(
                stream.getvalue(),
                "moco chibi nanashi")

    def write_test2(self):
        node = TextNode("<moco> chibi nanashi")
        with StringIO() as stream:
            node.write(stream)
            self.assertEqual(
                stream.getvalue(),
                "&lt;moco&gt; chibi nanashi")
