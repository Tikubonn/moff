
from .template import Builder
from moff.node import VideoNode, SourceNode, ParagraphNode, LinkNode, TextNode
from moff.mimetypes import video_mimetypes


class VideoSource:

    def __init__(self, src, type=None):
        self.src = src
        self.type = type

    def get_src(self):
        return self.src

    def get_type(self):
        if self.type:
            return self.type
        mime, encoding = video_mimetypes.guess_type(self.src)
        return mime

    def build_source_node(self):
        return SourceNode(
            src=self.get_src(),
            type=self.get_type())


class VideoBuilder (Builder):

    def __init__(self, sources=list(), thumbnail=None):
        self.sources = list(sources)
        self.thumbnail = thumbnail

    def add_source(self, source):
        self.sources.append(source)

    def set_thumbnail(self, thumbnail):
        self.thumbnail = thumbnail

    # override
    def add(self, anyone):
        raise Exception(".add() is unsupported.")

    # override
    def is_mergeable(self, builder):
        return False

    # override
    def merge(self, builder):
        raise Exception(".merge() is unsupported.")

    def build_alternative_node(self):
        if len(self.sources) == 0:
            raise Exception()
        else:
            source = self.sources[0]
            return ParagraphNode(nodes=[
                TextNode(
                    "Your browser has not supported playing video with HTML5."),
                TextNode("You can download video from "),
                LinkNode(
                    href=source.get_src(),
                    target="_blank",
                    nodes=[
                        TextNode("here")
                    ]),
                TextNode(".")
            ])

    # override
    def build_node(self):
        if len(self.sources) == 0:
            raise Exception()
        elif len(self.sources) == 1:
            source = self.sources[0]
            vnode = VideoNode(
                src=source.get_src(),
                poster=self.thumbnail,
                preload="none",
                controls=True,
                nodes=[
                    self.build_alternative_node()
                ])
            return vnode
        else:
            vnode = VideoNode(
                poster=self.thumbnail,
                preload="none",
                controls=True)
            for source in self.sources:
                vnode.add_node(source.build_source_node())
            vnode.add_node(
                self.build_alternative_node())
            return vnode
