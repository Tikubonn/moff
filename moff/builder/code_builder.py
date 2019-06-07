
from .template import Builder
from moff.node import CodeNode


class CodeBuilder (Builder):

    def __init__(self, code, language=None):
        self.code = code
        self.language = language

    # override
    def add(self, node):
        raise Exception(".add() is unsupported.")

    # override
    def is_mergeable(self, builder):
        return False

    # override
    def merge(self, builder):
        raise Exception(".merge() is unsupported.")

    # override
    def build_node(self):
        return CodeNode(self.code, language=self.language)
