
from unittest import TestCase
from moff.parser import Parser
from moff.node import LinkNode, PictureNode, SourceNode, ImageNode
from moff.attribute import Srcset, Sizes, SrcsetAttribute, SizesAttribute
from moff.unit import Width, Resolution


class TestReadImage (TestCase):

    def test_parse1(self):
        parser = Parser()
        node1 = parser.parse_string(
            "@image example.png\n" +
            "@image @alt alt text.\n" +
            "@image @title title text.")
        node2 = LinkNode(
            href="example.png",
            target="_blank",
            nodes=[
                ImageNode(
                    src="example.png",
                    alt="alt text.",
                    title="title text.",
                    decoding="async")
            ])
        self.assertEqual(str(node1), str(node2))

    def test_parse2(self):
        parser = Parser()
        node1 = parser.parse_string(
            "@image example.png\n" +
            "@image @case @src example1x.png 1x\n" +
            "@image @case @src example2x.png 2x")
        node2 = LinkNode(
            href="example.png",
            target="_blank",
            nodes=[
                ImageNode(
                    src="example.png",
                    srcset=SrcsetAttribute([
                        Srcset("example1x.png", width=Resolution(1)),
                        Srcset("example2x.png", width=Resolution(2))
                    ]),
                    decoding="async")
            ])
        self.assertEqual(str(node1), str(node2))

    def test_parse3(self):
        parser = Parser()
        node1 = parser.parse_string(
            "@image example.png\n" +
            "@image @case @src example1x.webp 1x\n" +
            "@image @case @src example2x.webp 2x\n" +
            "@image @case @type image/webp\n" +
            "@image @case\n" +
            "@image @case @src example1x.png 1x\n" +
            "@image @case @src example2x.png 2x\n")
        node2 = LinkNode(
            href="example.png",
            target="_blank",
            nodes=[
                PictureNode(nodes=[
                    SourceNode(
                        srcset=SrcsetAttribute([
                            Srcset("example1x.webp", width=Resolution(1)),
                            Srcset("example2x.webp", width=Resolution(2))
                        ]),
                        type="image/webp"
                    ),
                    SourceNode(
                        srcset=SrcsetAttribute([
                            Srcset("example1x.png", width=Resolution(1)),
                            Srcset("example2x.png", width=Resolution(2))
                        ]),
                        type="image/png"
                    ),
                    ImageNode(
                        src="example.png",
                        decoding="async")
                ])
            ])
        self.assertEqual(str(node1), str(node2))

    def test_parse4(self):
        parser = Parser()
        node1 = parser.parse_string(
            "@image example.png\n" +
            "@image @case @src example1x.webp 1x\n" +
            "@image @case @src example2x.webp 2x\n" +
            "@image @case\n" +
            "@image @case @src example1x.png 1x\n" +
            "@image @case @src example2x.png 2x")
        node2 = LinkNode(
            href="example.png",
            target="_blank",
            nodes=[
                PictureNode(nodes=[
                    SourceNode(
                        srcset=SrcsetAttribute([
                            Srcset("example1x.webp", width=Resolution(1)),
                            Srcset("example2x.webp", width=Resolution(2))
                        ]),
                        type="image/webp"
                    ),
                    SourceNode(
                        srcset=SrcsetAttribute([
                            Srcset("example1x.png", width=Resolution(1)),
                            Srcset("example2x.png", width=Resolution(2))
                        ]),
                        type="image/png"
                    ),
                    ImageNode(
                        src="example.png",
                        decoding="async")
                ])
            ])
        self.assertEqual(str(node1), str(node2))

    def test_parse5(self):
        parser = Parser()
        node1 = parser.parse_string(
            "@image example.png\n" +
            "@image @case @src example1x.webp 1x\n" +
            "@image @case @src example2x.webp 2x\n" +
            "@image @case @type image/webp")
        node2 = LinkNode(
            href="example.png",
            target="_blank",
            nodes=[
                PictureNode(nodes=[
                    SourceNode(
                        srcset=SrcsetAttribute([
                            Srcset("example1x.webp", width=Resolution(1)),
                            Srcset("example2x.webp", width=Resolution(2))
                        ]),
                        type="image/webp"
                    ),
                    ImageNode(
                        src="example.png",
                        decoding="async")
                ])
            ])
        self.assertEqual(str(node1), str(node2))

    def test_parse6(self):
        parser = Parser()
        node1 = parser.parse_string(
            "@image example.png\n" +
            "@image @case @src example1x.webp 1x\n" +
            "@image @case @src example2x.webp 2x\n" +
            "@image @case @type image/webp\n" +
            "@image @case @media (max-width: 640px)")
        node2 = LinkNode(
            href="example.png",
            target="_blank",
            nodes=[
                PictureNode(nodes=[
                    SourceNode(
                        srcset=SrcsetAttribute([
                            Srcset("example1x.webp", width=Resolution(1)),
                            Srcset("example2x.webp", width=Resolution(2))
                        ]),
                        type="image/webp",
                        media="(max-width: 640px)"
                    ),
                    ImageNode(
                        src="example.png",
                        decoding="async")
                ])
            ])
        self.assertEqual(str(node1), str(node2))

    def test_parse7(self):
        parser = Parser()
        node1 = parser.parse_string(
            "@image example.png\n" +
            "@image @case @src example-square.png 320w\n" +
            "@image @case @src example-full.png 640w")
        node2 = LinkNode(
            href="example.png",
            target="_blank",
            nodes=[
                PictureNode(nodes=[
                    SourceNode(
                        srcset=SrcsetAttribute([
                            Srcset("example-square.png", width=Width(320)),
                            Srcset("example-full.png", width=Width(640))
                        ]),
                        type="image/png"
                    ),
                    ImageNode(
                        src="example.png",
                        decoding="async")
                ])
            ])
        self.assertEqual(str(node1), str(node2))
