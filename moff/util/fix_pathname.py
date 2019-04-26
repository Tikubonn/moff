
from urllib.parse import urlparse, urlunparse, ParseResult
from pathlib import Path

def fix_pathname (src, options=dict()):
  parsed = urlparse(src)
  if not parsed.scheme:
    path = Path(parsed.path)
    prefix = Path(options.get("prefix_path", ""))
    fixed = ParseResult(
      scheme = parsed.scheme,
      netloc = parsed.netloc,
      path = prefix.joinpath(path).as_posix(),
      params = parsed.params,
      query = parsed.query,
      fragment = parsed.fragment)
    return urlunparse(fixed)
  return src
