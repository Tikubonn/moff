
from .escape_with_backslash import escape_with_backslash
from io import StringIO


def read_until_string(stream, untilstr, use_escape=True, eof_is_error=True):
    with StringIO() as readstr:
        previous = ""
        while True:
            character = stream.get()
            if not character:
                if eof_is_error:
                    raise Exception()
                else:
                    break
            prev = (character + previous)
            char, previous = prev[len(untilstr):], prev[:len(untilstr)]
            if use_escape and char == "\\":
                if previous:
                    char, previous = previous[-1], previous[:-1]
                    readstr.write(
                        escape_with_backslash(char))
                else:
                    char = stream.get()
                    readstr.write(
                        escape_with_backslash(char))
            elif previous == untilstr:
                readstr.write(char)
                stream.release(previous)
                break
            else:
                readstr.write(char)
        return readstr.getvalue()
