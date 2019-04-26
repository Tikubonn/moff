
from .syntax_node import SyntaxNode
from io import StringIO

class SyntaxTable (SyntaxNode):
  
  def __init__ (self, default_function=None):
    super().__init__(character=None, function=default_function)
  
  def register (self, code, function):
    node = self
    for character in code:
      node = node.dig(character)
    node.set_function(function)
  
  def register_default (self, function):
    self.set_function(function)
  
  def is_syntax_character (self, character):
    return self.has_character(character)
  
  def try_call (self, node, preread, stream, *arguments, **keywords):
    function = node.get_function()
    if function:
      return function(preread, stream, *arguments, **keywords)
    else:
      function = self.get_function()
      if function:
        return function(preread, stream, *arguments, **keywords)
      else:
        raise Error("syntax could not found.")
  
  def read (self, stream, *arguments, **keywords):
    with StringIO() as preread:
      node = self
      while True:
        character = stream.peek()
        if not character:
          return self.try_call(
            node,
            preread.getvalue(), 
            stream,
            *arguments,
            **keywords)
        if not node.has_character(character):
          return self.try_call(
            node,
            preread.getvalue(),
            stream,
            *arguments,
            **keywords)
        node = node.get(character)
        preread.write(character)
        stream.get()
      return None

# default block syntaxes

from .read_ordered_list import read_ordered_list
from .read_unordered_list import read_unordered_list
from .read_paragraph import read_paragraph
from .read_end_line_block import read_end_line_block
from .read_quotation import read_quotation, read_quotation_cite
from .read_heading import read_heading1, read_heading2, read_heading3, read_heading4, read_heading5, read_heading6
from .read_code import read_code
from .read_html import read_html_block
from .read_table import read_table
from .read_image import read_image, read_image_alt, read_image_title, read_image_link, read_image_case, read_image_srccase, read_image_sizecase, read_image_mediacase, read_image_typecase
from .read_video import read_video, read_video_src, read_video_thumbnail
from .read_audio import read_audio, read_audio_src

default_block_syntax_table = SyntaxTable()
default_block_syntax_table.register_default(read_paragraph)
default_block_syntax_table.register("- ", read_ordered_list)
default_block_syntax_table.register("* ", read_unordered_list)
default_block_syntax_table.register("\n", read_end_line_block)
default_block_syntax_table.register("> ", read_quotation)
default_block_syntax_table.register("# ", read_heading1)
default_block_syntax_table.register("## ", read_heading2)
default_block_syntax_table.register("### ", read_heading3)
default_block_syntax_table.register("#### ", read_heading4)
default_block_syntax_table.register("##### ", read_heading5)
default_block_syntax_table.register("###### ", read_heading6)
default_block_syntax_table.register("```", read_code)
default_block_syntax_table.register(">> ", read_quotation_cite)
default_block_syntax_table.register("<", read_html_block)
default_block_syntax_table.register("|", read_table)
default_block_syntax_table.register("@image ", read_image)
default_block_syntax_table.register("@image @alt ", read_image_alt)
default_block_syntax_table.register("@image @title ", read_image_title)
default_block_syntax_table.register("@image @link ", read_image_link)
default_block_syntax_table.register("@image @case", read_image_case)
default_block_syntax_table.register("@image @case @src ", read_image_srccase)
default_block_syntax_table.register("@image @case @size ", read_image_sizecase)
default_block_syntax_table.register("@image @case @media ", read_image_mediacase)
default_block_syntax_table.register("@image @case @type ", read_image_typecase)
default_block_syntax_table.register("@video ", read_video)
default_block_syntax_table.register("@video @src ", read_video_src)
default_block_syntax_table.register("@video @thumbnail ", read_video_thumbnail)
default_block_syntax_table.register("@audio ", read_audio)
default_block_syntax_table.register("@audio @src ", read_audio_src)

# default inline syntaxes

from .read_text import read_text
from .read_escape import read_escape
from .read_end_line import read_end_line
from .read_newline import read_newline 
from .read_inline_code import read_inline_code
from .read_url import read_url
from .read_link import read_link
from .read_html import read_html
from .read_delete import read_delete
from .read_emphasis import read_emphasis
from .read_strong import read_strong
from .read_table import read_table_separator
from .read_whitespace import read_whitespace

default_inline_syntax_table = SyntaxTable()
default_inline_syntax_table.register_default(read_text)
default_inline_syntax_table.register("\\", read_escape)
default_inline_syntax_table.register("\n", read_end_line)
default_inline_syntax_table.register("  ", read_newline)
default_inline_syntax_table.register("`", read_inline_code)
default_inline_syntax_table.register("http://", read_url)
default_inline_syntax_table.register("https://", read_url)
default_inline_syntax_table.register("[", read_link)
default_inline_syntax_table.register("<", read_html)
default_inline_syntax_table.register("~~", read_delete)
default_inline_syntax_table.register("*", read_emphasis)
default_inline_syntax_table.register("**", read_strong)
default_inline_syntax_table.register("|", read_table_separator)
default_inline_syntax_table.register(" ", read_whitespace)
