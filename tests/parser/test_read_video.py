
from unittest import TestCase
from moff.parser import Parser
from moff.node import VideoNode, SourceNode, ParagraphNode, LinkNode, TextNode

class TestReadVideo (TestCase):
  
  def test_parse1 (self):
    parser = Parser()
    node1 = parser.parse_string("@video example.mp4")
    node2 = VideoNode(
      src = "example.mp4",
      preload = "none",
      controls = True,
      nodes=[
        ParagraphNode(nodes=[
          TextNode("Your browser has not supported playing video with HTML5."),
          TextNode("You can download video from "),
          LinkNode(
            href = "example.mp4",
            target = "_blank",
            nodes = [
              TextNode("here")
            ]),
          TextNode(".")
        ])
      ])
    self.assertEqual(str(node1), str(node2))
  
  def test_parse2 (self):
    parser = Parser()
    node1 = parser.parse_string("@video example.mp4\n@video @thumbnail thumbnail.jpg")
    node2 = VideoNode(
      src = "example.mp4",
      poster = "thumbnail.jpg",
      preload = "none",
      controls = True,
      nodes=[
        ParagraphNode(nodes=[
          TextNode("Your browser has not supported playing video with HTML5."),
          TextNode("You can download video from "),
          LinkNode(
            href = "example.mp4",
            target = "_blank",
            nodes = [
              TextNode("here")
            ]),
          TextNode(".")
        ])
      ])
    self.assertEqual(str(node1), str(node2))
  
  def test_parse3 (self):
    parser = Parser()
    node1 = parser.parse_string("@video example.mp4\n@video @src example.mp4\n@video @src example.webm video/webm")
    node2 = VideoNode(
      preload = "none",
      controls = True,
      nodes=[
        SourceNode(
          src = "example.mp4",
          type = "video/mp4"),
        SourceNode(
          src = "example.mp4",
          type = "video/mp4"),
        SourceNode(
          src = "example.webm",
          type = "video/webm"),
        ParagraphNode(nodes=[
          TextNode("Your browser has not supported playing video with HTML5."),
          TextNode("You can download video from "),
          LinkNode(
            href = "example.mp4",
            target = "_blank",
            nodes = [
              TextNode("here")
            ]),
          TextNode(".")
        ])
      ])
    self.assertEqual(str(node1), str(node2))
