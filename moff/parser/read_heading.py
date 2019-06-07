
from moff.builder import HeadingBuilder


def read_heading1(preread, stream, indentation, parser, options):
    return HeadingBuilder(1)


def read_heading2(preread, stream, indentation, parser, options):
    return HeadingBuilder(2)


def read_heading3(preread, stream, indentation, parser, options):
    return HeadingBuilder(3)


def read_heading4(preread, stream, indentation, parser, options):
    return HeadingBuilder(4)


def read_heading5(preread, stream, indentation, parser, options):
    return HeadingBuilder(5)


def read_heading6(preread, stream, indentation, parser, options):
    return HeadingBuilder(6)
