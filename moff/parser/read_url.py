
from moff.node import LinkNode, TextNode
from moff.util import read_while
from io import StringIO
import string

URL_CHARS = set(
  string.ascii_letters + 
  string.digits + 
  "-" + "." + "_" + "~" +
  "!" + "#" + "$" + "&" + 
  "'" + "(" + ")" + "*" + 
  "+" + "," + "/" + ":" + 
  ";" + "=" + "?" + "@" + 
  "[" + "]")

def read_url (preread, stream, parser, options):
  with StringIO() as readstr:
    readstr.write(preread)
    read = read_while(stream, URL_CHARS, eof_is_error=False)
    readstr.write(read)
    linknode = LinkNode(
      href = readstr.getvalue(),
      target = "_blank")
    linknode.add_node(
      TextNode(readstr.getvalue()))
    return linknode
