
from moff.node import TextNode
from moff.util import escape_with_backslash


def read_escape(preread, stream, parser, options):
    character = stream.get()
    if not character:
        raise Error("reached eof.")
    return TextNode(
        escape_with_backslash(character))
