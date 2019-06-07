
from moff.node import TextNode
from io import StringIO


def read_text(preread, stream, parser, options):
    with StringIO() as readstr:
        readstr.write(preread)
        while True:
            character = stream.peek()
            if not character:
                break
            if parser.is_inline_syntax_character(character):
                break
            stream.get()
            readstr.write(character)
        return TextNode(readstr.getvalue())
