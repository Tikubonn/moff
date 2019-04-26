
from moff.builder import AudioBuilder, AudioSource, AudioSourceAdapter
from moff.util import read_line, read_until, read_whitespace

# @audio ...
def read_audio (preread, stream, indentation, parser, options=dict()):
  read1 = read_line(stream).strip()
  audio = AudioBuilder()
  if read1:
    source = AudioSource(read1)
    audio.add_source(source)
  return audio

# @audio @src path type
def read_audio_src (preread, stream, indentation, parser, options=dict()):
  read1 = read_until(stream, "\n ").strip()
  read_whitespace(stream)
  read2 = read_line(stream).strip()
  source = AudioSource(
    src = read1,
    type = read2 if read2 else None)
  return AudioSourceAdapter(source)
