
from .end_line import EndLine
from .syntax_table import SyntaxTable, default_inline_syntax_table, default_block_syntax_table
from moff.builder import RootBuilder
from moff.node import node
from moff.stream import CacheStream
from io import StringIO

def read_indentation (cstream):
  count = 0
  while True:
    character = cstream.peek()
    if character == " ":
      count += 1
      cstream.get()
    else:
      return count

class Parser:
  
  def __init__ (
    self,
    block_syntax_table = default_block_syntax_table,
    inline_syntax_table = default_inline_syntax_table,
    options = dict()):
    self.block_syntax_table = block_syntax_table
    self.inline_syntax_table = inline_syntax_table
    self.options = dict(options)
  
  def is_block_syntax_character (self, character):
    return self.block_syntax_table.is_syntax_character(character)
  
  def is_inline_syntax_character (self, character):
    return self.inline_syntax_table.is_syntax_character(character)
  
  def parse_string (self, source):
    with StringIO(source) as stream:
      return self.parse(stream)
  
  def parse (self, stream):
    cstream = CacheStream(stream)
    root = RootBuilder()
    builder = None 
    while not cstream.is_eof():
      bu = self.parse_line(cstream)
      if bu:
        if builder:
          if builder.is_mergeable(bu):
            builder = builder.merge(bu)
          elif bu.is_mergeable(builder):
            builder = bu.merge(builder)
          else:
            root.add(builder)
            builder = bu
        else:
          builder = bu
      else:
        if builder:
          root.add(builder)
          builder = bu
        else:
          pass
    if builder:
      root.add(builder)
    return node(root)
  
  def parse_line (self, cstream):
    builder = None
    try:
      indentation = read_indentation(cstream)
      # read block syntax
      builder = self.block_syntax_table.read(cstream, indentation, self, self.options)
      # read inline syntax
      while not cstream.is_eof():
        node = self.inline_syntax_table.read(cstream, self, self.options)
        if not node:
          break
        builder.add(node)
    except EndLine:
      return builder
    return builder
  