
from io import StringIO

default_sanitize_table = {
  "<": "&lt;",
  ">": "&gt;",
  "&": "&amp;",
  '"': "&quot;",
  "'": "&#39;"
}

def sanitize (source, sanitize_table=default_sanitize_table):
  with StringIO() as stream:
    for character in source:
      if character in sanitize_table:
        stream.write(sanitize_table[character])
      else:
        stream.write(character)
    return stream.getvalue()
