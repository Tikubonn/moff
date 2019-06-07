
from io import StringIO


def read_paren(stream):
    with StringIO() as readstr:
        # open paren
        character = stream.get()
        if character != "(":
            raise Exception()
        readstr.write(character)
        # until close paren
        while True:
            character = stream.peek()
            if not character:
                raise Exception()
            elif character == "(":
                read = read_paren(stream)
                readstr.write(read)
            elif character == ")":
                readstr.write(character)
                stream.get()
                break
            else:
                readstr.write(character)
                stream.get()
        return readstr.getvalue()


def read_media_query(stream):
    with StringIO() as readstr:
        while True:
            character = stream.peek()
            if not character:
                raise Exception()
            elif character == "(":
                read = read_paren(stream)
                readstr.write(read)
            elif character in "\n ":
                break
            else:
                readstr.write(character)
                stream.get()
        return readstr.getvalue()
