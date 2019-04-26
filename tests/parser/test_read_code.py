
from unittest import TestCase
from moff.parser import Parser
from moff.node import CodeNode

class TestReadCode (TestCase):
  
  def test_parse1 (self):
    parser = Parser()
    node1 = parser.parse_string(
      "```\n" + 
      "<b>example</b>\n" + 
      "```")
    node2 = CodeNode("<b>example</b>")
    self.assertEqual(str(node1), str(node2))
  
  def test_parse2 (self):
    parser = Parser()
    node1 = parser.parse_string(
      "```html\n" + 
      "<b>example</b>\n" + 
      "```")
    node2 = CodeNode("<b>example</b>", language="html")
    self.assertEqual(str(node1), str(node2))
  