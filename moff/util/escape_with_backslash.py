
ESCAPE_TABLE = {
  "a": "\a",
  "b": "\b",
  "f": "\f",
  "n": "\n",
  "r": "\r",
  "t": "\t",
  "v": "\v",
  "0": "\0",
}

def escape_with_backslash (character):
  return ESCAPE_TABLE.get(character, character)
