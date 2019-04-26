
from moff.builder import QuotationBuilder, QuotationRootBuilder, QuotationCiteAdapter
from moff.util import read_line

#
# > ... 
#

def read_quotation (preread, stream, indentation, parser, options):
  builder = QuotationBuilder(indentation)
  return QuotationRootBuilder(builder)

#
# >> ...
#

def read_quotation_cite (preread, stream, indentation, parser, options):
  line = read_line(stream)
  cite = None
  if line:
    cite = line.strip()
  return QuotationCiteAdapter(cite=cite)
  