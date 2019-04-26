
# Moff

\| [日本語](README.ja.md) \| English \|

Moff is a Markdown dialects.
I wrote this for mine with Python.
Moff has supported picture, video and audio for multiple device.

```markdown
# What is 
# Moff 

Moff is a Markdown dialects.
Moff has supported picture, video and audio for multiple device.

@image example.jpg
@image @case @src example1x.jpg 1x
@image @case @src example2x.jpg 2x

@video 
@video @src example.mp4
@video @src example.webm
@video @thumbnail thumbnail.jpg

@audio 
@audio @src example.mp3
@audio @src example.webm
```

```html
<h1>What is Moff</h1>
<p>
  Moff is a Markdown dialects.
  Moff has supported picture, video and audio for multiple device.
</p>
<a href="example.jpg" target="_blank">
  <img src="example.jpg" srcset="example1x.jpg 1x, example2x.jpg 2x" decoding="async">
</a>
<video preload="none" poster="thumbnail.jpg" controls>
  <source src="example.mp4" type="video/mpeg">
  <source src="example.webm" type="video/webm">
</video>
<audio preload="none" controls>
  <source src="example.mp3" type="audio/mpeg">
  <source src="example.webm" type="audio/webm">
</audio>
```

## Using as library.

you can use `Parser` class from `moff.parser` module for translating Moff source code to HTML structure. 
`.parse()` method parse from input file. `.parse_string()` method parse from string.
if you want to know detail, you can read here.

```python
from moff.parser import Parser
from sys import stdout

with open("input.mh", "r") as instream:
  parser = Parser()
  node = parser.parse(instream)
  node.write(stdout) # or print(str(node))
```

## Using with shell.

you can execute Moff from shell, because Moff prepared `__main__.py`.

```bash
python -m moff
```

```bash
python -m moff --input-file "input.mh" --output-file "output.html"
```

Moff has supported these options.

| オプション | 概要 | 
| ---- | ---- |
| `--input-file` | take a file name for input. if you didn't use this option, Moff use the *standard-input*. | 
| `--output-file` | take a file name for output. if you didn't use this option, Moff use the *standard-output*. | 
| `--prefix-path` | take the prefix path that concatenate to picture, video and audio file path. | 

## Specification

you can read detail from wiki.

## How to install

Moff has `setup.py`, so you can install this package with this command.

```bash
python setup.py install
```

## License

Moff released under the [MIT License](LICENSE).
