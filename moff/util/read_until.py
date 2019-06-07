
from .escape_with_backslash import escape_with_backslash
from io import StringIO


def read_until(stream, untilset, use_escape=True, eof_is_error=True):
    with StringIO() as readstr:
        while True:
            character = stream.peek()
            if not character:
                if eof_is_error:
                    raise Exception()
                else:
                    break
            elif use_escape and character == "\\":
                stream.get()
                character = stream.get()
                readstr.write(
                    escape_with_backslash(character))
            elif character in untilset:
                break
            else:
                readstr.write(character)
                stream.get()
        return readstr.getvalue()
