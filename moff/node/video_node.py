
from .template import CollectionNode


class VideoNode (CollectionNode):

    def __init__(
            self,
            src=None,
            autoplay=None,
            buffered=None,
            controls=None,
            crossorigin=None,
            height=None,
            intrinsicsize=None,
            loop=None,
            muted=None,
            preload=None,
            playsinline=None,
            poster=None,
            width=None,
            nodes=list()):
        super().__init__(nodes)
        self.src = src
        self.autoplay = autoplay
        self.buffered = buffered
        self.controls = controls
        self.crossorigin = crossorigin
        self.height = height
        self.intrinsicsize = intrinsicsize
        self.loop = loop
        self.muted = muted
        self.preload = preload
        self.playsinline = playsinline
        self.poster = poster
        self.width = width

    def write_attributes(self, stream):
        if self.src is not None:
            stream.write(" src=\"%s\"" % (self.src,))
        if self.autoplay:
            stream.write(" autoplay")
        if self.buffered is not None:
            stream.write(" buffered=\"%s\"" % (self.buffered,))
        if self.controls:
            stream.write(" controls")
        if self.crossorigin is not None:
            stream.write(" crossorigin=\"%s\"" % (self.crossorigin,))
        if self.height is not None:
            stream.write(" height=\"%s\"" % (self.height,))
        if self.intrinsicsize is not None:
            stream.write(" intrinsicsize=\"%s\"" % (self.intrinsicsize,))
        if self.loop:
            stream.write(" loop")
        if self.muted:
            stream.write(" muted")
        if self.preload is not None:
            stream.write(" preload=\"%s\"" % (self.preload,))
        if self.playsinline is not None:
            stream.write(" playsinline=\"%s\"" % (self.playsinline,))
        if self.poster is not None:
            stream.write(" poster=\"%s\"" % (self.poster,))
        if self.width is not None:
            stream.write(" width=\"%s\"" % (self.width,))

    # override
    def write(self, stream):
        stream.write("<video")
        self.write_attributes(stream)
        stream.write(">")
        super().write(stream)
        stream.write("</video>")
