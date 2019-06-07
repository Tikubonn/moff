
from unittest import TestCase
from moff.parser import Parser
from moff.node import AudioNode, SourceNode, ParagraphNode, LinkNode, TextNode


class TestReadAudio (TestCase):

    def test_parse1(self):
        parser = Parser()
        node1 = parser.parse_string("@audio example.mp3")
        node2 = AudioNode(
            src="example.mp3",
            preload="none",
            controls=True,
            nodes=[
                ParagraphNode(nodes=[
                    TextNode(
                        "Your browser has not supported playing audio with HTML5."),
                    TextNode("You can download audio from "),
                    LinkNode(
                        href="example.mp3",
                        target="_blank",
                        nodes=[
                            TextNode("here")
                        ]),
                    TextNode(".")
                ])
            ])
        self.assertEqual(str(node1), str(node2))

    def test_parse2(self):
        parser = Parser()
        node1 = parser.parse_string(
            "@audio example.mp3\n@audio @src example.mp3\n@audio @src example.wav audio/wav")
        node2 = AudioNode(
            preload="none",
            controls=True,
            nodes=[
                SourceNode(
                    src="example.mp3",
                    type="audio/mpeg"),
                SourceNode(
                    src="example.mp3",
                    type="audio/mpeg"),
                SourceNode(
                    src="example.wav",
                    type="audio/wav"),
                ParagraphNode(nodes=[
                    TextNode(
                        "Your browser has not supported playing audio with HTML5."),
                    TextNode("You can download audio from "),
                    LinkNode(
                        href="example.mp3",
                        target="_blank",
                        nodes=[
                            TextNode("here")
                        ]),
                    TextNode(".")
                ])
            ])
        self.assertEqual(str(node1), str(node2))
