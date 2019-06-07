
class Sizes:

    def __init__(self, width, media=None):
        self.width = width
        self.media = media

    def write(self, stream):
        if self.media:
            stream.write(str(self.media))
            stream.write(" ")
        stream.write(str(self.width))


class SizesAttribute:

    def __init__(self, sizeses=list()):
        self.sizeses = list()

    def __len__(self):
        return len(self.sizeses)

    def __iter__(self):
        return iter(self.sizeses)

    def add(self, sizes):
        if not isinstance(sizes, Sizes):
            raise TypeError("%s is not %s instance." % (sizes, Sizes.__name__))
        self.sizeses.append(sizes)

    def write(self, stream):
        if self.sizeses:
            stream.write(" sizes=\"")
            for index, sizes in enumerate(self.sizeses):
                if 0 < index:
                    stream.write(", ")
                sizes.write(stream)
            stream.write("\"")
