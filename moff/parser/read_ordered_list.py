
from moff.builder import OrderedListBuilder, OrderedListRootBuilder

def read_ordered_list (preread, stream, indentation, parser, options):
  builder = OrderedListBuilder(indentation)
  return OrderedListRootBuilder(builder)
