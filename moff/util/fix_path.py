
from urllib.parse import urlparse, urlunparse, ParseResult
from pathlib import Path


def fix_path(src, options=dict()):
    if src.startswith("http://"):
        return src
    elif src.startswith("https://"):
        return src
    elif src.startswith("/"):
        return src
    else:
        parsed = urlparse(src)
        if parsed.path:
            path = Path(parsed.path)
            prefix = Path(options.get("prefix_path", ""))
            fixed = ParseResult(
                scheme=parsed.scheme,
                netloc=parsed.netloc,
                path=prefix.joinpath(path).as_posix(),
                params=parsed.params,
                query=parsed.query,
                fragment=parsed.fragment)
            return urlunparse(fixed)
        return src
