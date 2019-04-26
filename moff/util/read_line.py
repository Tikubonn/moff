
from .read_until import read_until
from io import StringIO

def read_line (stream, use_escape=True, eof_is_error=False):
  return read_until(stream, "\n", use_escape=use_escape, eof_is_error=eof_is_error)
