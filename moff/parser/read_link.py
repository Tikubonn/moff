
from moff.node import LinkNode, TextNode
from moff.util import read_until, read_while, fix_path
from urllib.parse import urlparse


def make_link(text, href):
    parsed = urlparse(href)
    if (not parsed.scheme and
        not parsed.netloc and
        not parsed.path and
        not parsed.params and
        not parsed.query and
        not parsed.username and
        not parsed.password and
        not parsed.hostname and
        not parsed.port and
            parsed.fragment):
        return LinkNode(
            href=href,
            nodes=[
                TextNode(text)
            ])
    else:
        return LinkNode(
            href=href,
            target="_blank",
            nodes=[
                TextNode(text)
            ])

#
# [...](...)
# [...]
#


def read_link(preread, stream, parser, options):
    read1 = read_until(stream, "]", use_escape=True).strip()  # [...]
    stream.get()
    if stream.peek() == "(":
        stream.get()
        read2 = read_until(stream, ")", use_escape=True).strip()  # (...)
        stream.get()
        return make_link(read1, fix_path(read2))
    else:
        lnode = LinkNode(href=read1, target="_blank")
        return make_link(read1, fix_path(read1))
