
from .streamlike import Streamlike


class CacheStream (Streamlike):

    def __init__(self, stream):
        self.stream = stream
        self.cache = ""

    # override
    def peek(self):
        if not self.cache:
            character = self.stream.read(1)
            self.cache = character
            return character
        else:
            return self.cache[0]

    # override
    def get(self):
        if not self.cache:
            return self.stream.read(1)
        else:
            character = self.cache[0]
            self.cache = self.cache[1:]
            return character
            return character

    # override
    def read(self, size):
        if not self.cache:
            return self.stream.read(size)
        else:
            preread = self.cache[:size]
            self.cache = self.cache[size:]
            read = self.stream.read(size - len(preread))
            return preread + read

    # override
    def release(self, data):
        self.cache = data + self.cache
