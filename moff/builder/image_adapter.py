
from .template import Adapter
from .image_builder import ImageBuilder


class ImageAdapter (Adapter):

    # override
    def is_mergeable(self, builder):
        return isinstance(builder, ImageBuilder)


class ImageAltAdapter (ImageAdapter):

    def __init__(self, alt):
        self.alt = alt

    # override
    def merge(self, builder):
        builder.add_alt(self.alt)
        return builder


class ImageTitleAdapter (ImageAdapter):

    def __init__(self, title):
        self.title = title

    # override
    def merge(self, builder):
        builder.add_title(self.title)
        return builder


class ImageLinkAdapter (ImageAdapter):

    def __init__(self, link):
        self.link = link

    # override
    def merge(self, builder):
        builder.set_srcset(self.link)
        return builder


class ImageCaseAdapter (ImageAdapter):

    # override
    def merge(self, builder):
        builder.next_case()
        return builder


class ImageSrcCaseAdapter (ImageAdapter):

    def __init__(self, srcset):
        self.srcset = srcset

    # override
    def merge(self, builder):
        builder.add_srcset(self.srcset)
        return builder


class ImageSizeCaseAdapter (ImageAdapter):

    def __init__(self, sizes):
        self.sizes = sizes

    # override
    def merge(self, builder):
        builder.add_sizes(self.sizes)
        return builder


class ImageMediaCaseAdapter (ImageAdapter):

    def __init__(self, media):
        self.media = media

    # override
    def merge(self, builder):
        builder.set_media(self.media)
        return builder


class ImageTypeCaseAdapter (ImageAdapter):

    def __init__(self, type):
        self.type = type

    # override
    def merge(self, builder):
        builder.set_type(self.type)
        return builder


class ImageAppendixAdapter (ImageAdapter):

    # override
    def merge(self, builder):
        builder.set_appendix(True)
        return builder
