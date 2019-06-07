
from unittest import TestCase
from moff.node import ImageNode
from io import StringIO


class TestImageNode (TestCase):

    def test_write1(self):
        inode = ImageNode("example.png")
        with StringIO() as stream:
            inode.write(stream)
            self.assertEqual(
                stream.getvalue(),
                "<img src=\"example.png\">")

    def test_write2(self):
        inode = ImageNode("example.png", alt="alt")
        with StringIO() as stream:
            inode.write(stream)
            self.assertEqual(
                stream.getvalue(),
                "<img src=\"example.png\" alt=\"alt\">")
