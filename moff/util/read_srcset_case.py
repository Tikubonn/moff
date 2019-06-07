
from moff.unit import Width, Resolution
from .read_whitespace import read_whitespace
from .read_while import read_while
from .read_line import read_line


def number(source):
    if "." in source:
        return float(source)
    return int(source)


def read_srcset_case(stream):
    read_whitespace(stream, use_escape=False,
                    eof_is_error=False)  # skip whitespace!
    if not stream.is_eof() and stream.peek() != "\n":
        num = read_while(stream, "1234567890.",
                         use_escape=False, eof_is_error=True).strip()
        unit = read_line(stream, use_escape=False, eof_is_error=False).strip()
        # check
        if not num:
            raise Exception()
        if not unit:
            raise Exception()
        # main
        if unit == "w":
            return Width(number(num))
        elif unit == "x":
            return Resolution(number(num))
        else:
            raise Exception()
    else:
        return None
