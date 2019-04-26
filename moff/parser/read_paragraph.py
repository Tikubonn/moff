
from moff.builder import ParagraphBuilder

def read_paragraph (preread, stream, indentation, parser, options):
  stream.release(preread)
  return ParagraphBuilder()
  