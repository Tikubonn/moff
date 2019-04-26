
from moff.builder import UnOrderedListBuilder, UnOrderedListRootBuilder

def read_unordered_list (preread, stream, indentation, parser, options):
  builder = UnOrderedListBuilder(indentation)
  return UnOrderedListRootBuilder(builder)
