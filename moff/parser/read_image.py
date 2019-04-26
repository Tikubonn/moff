
from moff.builder import ImageBuilder, ImageAltAdapter, ImageTitleAdapter, ImageLinkAdapter, ImageCaseAdapter, ImageSrcCaseAdapter, ImageSizeCaseAdapter, ImageMediaCaseAdapter, ImageTypeCaseAdapter
from moff.attribute import Srcset, Sizes
from moff.util import read_until, read_whitespace, read_line, read_media_query, read_srcset_case

# @image path

def read_image (preread, stream, indentation, parser, options=dict()):
  read1 = read_line(stream).strip()
  return ImageBuilder(src=read1)

# @image @alt ...

def read_image_alt (preread, stream, indentation, parser, options=dict()):
  read1 = read_line(stream).strip()
  return ImageAltAdapter(read1)

# @image @title ...

def read_image_title (preread, stream, indentation, parser, options=dict()):
  read1 = read_line(stream).strip()
  return ImageTitleAdapter(read1)

# @image @link ...

def read_image_link (preread, stream, indentation, parser, options=dict()):
  read1 = read_line(stream).strip()
  return ImageLinkAdapter(read1)

# @image @case

def read_image_case (preread, stream, indentation, parser, options=dict()):
  return ImageCaseAdapter()

# @image @sizecase path width

def read_image_srccase (preread, stream, indentation, parser, options=dict()):
  src = read_until(stream, " ", use_escape=True, eof_is_error=True).strip()
  read_whitespace(stream)
  width = read_srcset_case(stream)
  return ImageSrcCaseAdapter(Srcset(src=src, width=width))

# @image @case @type 

def read_image_sizecase (preread, stream, indentation, parser, options=dict()):
  read1 = read_media_query(stream, use_escape=True, eof_is_error=True).strip()
  read_whitespace(stream)
  read2 = read_line(stream, use_escape=True, eof_is_error=True).strip()
  if read2:
    return ImageSizeCaseAdapter(Sizes(width=read2, media=read1))
  else:
    return ImageSizeCaseAdapter(Sizes(width=read1))

# @image @mediacase

def read_image_mediacase (preread, stream, indentation, parser, options=dict()):
  read1 = read_line(stream, use_escape=True, eof_is_error=False)
  return ImageMediaCaseAdapter(read1)

# @image @typecase

def read_image_typecase (preread, stream, indentation, parser, options=dict()):
  read1 = read_line(stream, use_escape=True, eof_is_error=False)
  return ImageTypeCaseAdapter(read1)

# @image @appendix 

def read_image_appendix (preread, stream, indentation, parser, options=dict()):
  return ImageAppendixAdapter()
