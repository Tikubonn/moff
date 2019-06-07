
from moff.builder import CodeBuilder
from moff.util import read_line, read_until_string
from io import StringIO


def read_code(preread, stream, indentation, parser, options):
    language = read_line(stream, eof_is_error=True).strip()
    if not language:
        language = None
    read = read_until_string(
        stream, "```", use_escape=True, eof_is_error=True).strip()
    stream.read(3)  # skip
    return CodeBuilder(read, language=language)
