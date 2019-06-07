
from .template import Adapter
from .quotation_builder import QuotationBuilder, QuotationRootBuilder


class QuotationAdapter (Adapter):

    # override
    def is_mergeable(self, builder):
        return isinstance(builder, QuotationRootBuilder)


class QuotationCiteAdapter (QuotationAdapter):

    def __init__(self, cite):
        self.cite = cite

    # override
    def merge(self, builder):
        builder.get_builder().set_cite(self.cite)
        return builder
