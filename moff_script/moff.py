
from argparse import ArgumentParser, FileType
from moff.parser import Parser
from pathlib import Path

def __main ():
  argparser = ArgumentParser(
    description = "translate markdown like syntax to HTML."
  )
  argparser.add_argument(
    "-v",
    "--version",
    help = "print version and exit.",
    action = "version",
    version = "%(prog)s 1.0.0"
  )
  argparser.add_argument(
    "-f",
    "--input-file",
    help = "take an input file name. if you didn't use this option, moff use standard-input.",
    dest = "input_file",
    type = FileType(mode="r", encoding="utf-8"),
    default = "-"
  )
  argparser.add_argument(
    "-o",
    "--output-file",
    help = "take an output file name. if you didn't use this option, moff use standard-output.",
    dest = "output_file",
    type = FileType(mode="w", encoding="utf-8"),
    default = "-"
  )
  argparser.add_argument(
    "--prefix-path",
    help = "take an prefix path name for image, video and audio relative path.",
    dest = "prefix_path",
    type = str,
    default = ""
  )
  arguments = argparser.parse_args()
  # setup
  options = {
    "prefix_path": Path(arguments.prefix_path)
  }
  # parse and write
  parser = Parser(options=options)
  node = parser.parse(arguments.input_file)
  node.write(arguments.output_file)

def main ():
  try:
    __main()
  except KeyboardInterrupt:
    pass
