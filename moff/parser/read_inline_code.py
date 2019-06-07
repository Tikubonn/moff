
from moff.node import InlineCodeNode
from io import StringIO


def read_inline_code(preread, stream, parser, options):
    with StringIO() as readstr:
        while True:
            character = stream.get()
            if not character:
                raise Error("reached eof!")
            elif character == "`":
                break
            elif character == "\\":
                character = stream.get()
                readstr.write(character)
            else:
                readstr.write(character)
        return InlineCodeNode(readstr.getvalue())
