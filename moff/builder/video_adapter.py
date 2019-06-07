
from .template import Adapter
from .video_builder import VideoBuilder


class VideoAdapter (Adapter):

    # override
    def is_mergeable(self, builder):
        return isinstance(builder, VideoBuilder)


class VideoSourceAdapter (VideoAdapter):

    def __init__(self, source):
        self.source = source

    # override
    def merge(self, builder):
        builder.add_source(self.source)
        return builder


class VideoThumbnailAdapter (VideoAdapter):

    def __init__(self, thumbnail):
        self.thumbnail = thumbnail

    # override
    def merge(self, builder):
        builder.set_thumbnail(self.thumbnail)
        return builder
