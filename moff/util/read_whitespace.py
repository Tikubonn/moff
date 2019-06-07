
from .read_while import read_while


def read_whitespace(stream, use_escape=True, eof_is_error=True):
    return read_while(stream, " ", use_escape=use_escape, eof_is_error=eof_is_error)
