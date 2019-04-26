
import argparse
from .parser import Parser
from pathlib import Path

if __name__ == "__main__":
  argparser = argparse.ArgumentParser(
    description = "translate markdown like syntax to HTML."
  )
  argparser.add_argument(
    "-v",
    "--version",
    help = "print version and exit.",
    action = "version",
    version = "moff version 0.9.0"
  )
  argparser.add_argument(
    "-f",
    "--input-file",
    help = "take an input file name. if you didn't use this option, moff use standard-input.",
    dest = "input_file",
    type = argparse.FileType("r", encoding="utf-8"),
    default = "-"
  )
  argparser.add_argument(
    "-o",
    "--output-file",
    help = "take an output file name. if you didn't use this option, moff use standard-output.",
    dest = "output_file",
    type = argparse.FileType("w", encoding="utf-8"),
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
  # main
  parser = Parser()
  options = {
    "prefix_path": Path(arguments.prefix_path)
  }
  node = parser.parse(arguments.input_file, options=options)
  node.write(arguments.output_file)
