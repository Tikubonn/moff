
from moff.builder import HTMLBuilder
from moff.node import HTMLNode
from io import StringIO


def is_open_tag(source):
    return source[1] != "/" and source[-2] != "/"


def is_omit_tag(source):
    return source[-2] == "/"


def is_close_tag(source):
    return source[1] == "/"


def get_open_tagname(source):
    if source[0] != "<":
        raise Exception()
    with StringIO() as readstr:
        for character in source[1:]:
            if character in " >":
                break
            else:
                readstr.write(character)
        return readstr.getvalue()


def get_close_tagname(source):
    if source[:2] != "</":
        raise Exception()
    with StringIO() as readstr:
        for character in source[2:]:
            if character in " >":
                break
            else:
                readstr.write(character)
        return readstr.getvalue()

#
# <...>
#


def read_tag(stream):
    with StringIO() as readstr:
        # open paren
        character = stream.get()
        if not character:
            raise Exception()
        elif character != "<":
            raise Exception()
        else:
            readstr.write(character)
        # until close paren
        while True:
            character = stream.get()
            if not character:
                raise Exception()
            elif character == ">":
                readstr.write(character)
                break
            else:
                readstr.write(character)
        return readstr.getvalue()

#
# ... <
#


def read_inner(stream):
    with StringIO() as readstr:
        while True:
            character = stream.peek()
            if not character:
                raise Exception()
            elif character == "<":
                break
            else:
                readstr.write(character)
                stream.get()
        return readstr.getvalue()


class CloseParen (Exception):

    def __init__(self, tag):
        self.tag = tag

    def get_tag(self):
        return self.tag

#
# <...> ... </...>
# <.../>
#


def read(stream):
    with StringIO() as readstr:
        read1 = read_tag(stream)
        readstr.write(read1)
        if is_open_tag(read1):
            try:
                while True:
                    read2 = read_inner(stream)
                    readstr.write(read2)
                    read3 = read(stream)
                    readstr.write(read3)
            except CloseParen as cparen:
                openname = get_open_tagname(read1)
                closename = get_close_tagname(cparen.get_tag())
                if openname != closename:
                    raise Exception()
                readstr.write(cparen.get_tag())
            return readstr.getvalue()
        elif is_omit_tag(read1):
            return readstr.getvalue()
        elif is_close_tag(read1):
            raise CloseParen(read1)
        else:
            raise Exception()

#
# <...> ... </...>
# <.../>
#


def read_html(preread, stream, parser, options):
    stream.release(preread)
    html = read(stream)
    return HTMLNode(html)

#
# <...> ... </...>
# <.../>
#


def read_html_block(preread, stream, indentation, parser, options):
    builder = HTMLBuilder()
    html = read_html(preread, stream, parser, options)
    builder.add(html)
    return builder
