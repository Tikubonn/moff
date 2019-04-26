
from moff.builder import VideoBuilder, VideoSource, VideoSourceAdapter, VideoThumbnailAdapter
from moff.util import read_line, read_until, read_whitespace

# @video path
def read_video (preread, stream, indentation, parser, options=dict()):
  read1 = read_line(stream).strip()
  video = VideoBuilder()
  if read1:
    source = VideoSource(read1)
    video.add_source(source)
  return video

# @video @src path type
def read_video_src (preread, stream, indentation, parser, options=dict()):
  read1 = read_until(stream, "\n ").strip()
  read_whitespace(stream)
  read2 = read_line(stream).strip()
  return VideoSourceAdapter(
    VideoSource(
      src = read1,
      type = read2 if read2 else None
    ))

# @video @thumbnail ...
def read_video_thumbnail (preread, stream, indentation, parser, options=dict()):
  read1 = read_line(stream).strip()
  return VideoThumbnailAdapter(read1)
