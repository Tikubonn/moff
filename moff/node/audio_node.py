
from .template import CollectionNode


class AudioNode (CollectionNode):

    def __init__(
            self,
            src=None,
            autoplay=None,
            controls=None,
            crossorigin=None,
            loop=None,
            muted=None,
            preload=None,
            nodes=list()):
        super().__init__(nodes)
        self.src = src
        self.autoplay = autoplay
        self.controls = controls
        self.crossorigin = crossorigin
        self.loop = loop
        self.muted = muted
        self.preload = preload

    def write_attributes(self, stream):
        if self.src is not None:
            stream.write(" src=\"%s\"" % (self.src,))
        if self.autoplay:
            stream.write(" autoplay")
        if self.controls:
            stream.write(" controls")
        if self.crossorigin is not None:
            stream.write(" crossorigin=\"%s\"" % (self.crossorigin,))
        if self.loop:
            stream.write(" loop")
        if self.muted:
            stream.write(" muted")
        if self.preload is not None:
            stream.write(" preload=\"%s\"" % (self.preload,))

    # override
    def write(self, stream):
        stream.write("<audio")
        self.write_attributes(stream)
        stream.write(">")
        super().write(stream)
        stream.write("</audio>")
