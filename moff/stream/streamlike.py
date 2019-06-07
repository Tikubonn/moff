
from abc import ABC, abstractmethod


class Streamlike (ABC):

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def read(self, count):
        pass

    def is_eof(self):
        return not self.peek()
