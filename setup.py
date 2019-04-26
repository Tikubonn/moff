
from setuptools import setup, find_packages

setup(
  name = "moff",
  version = "1.0",
  description = "Moff is a markdown dialect that has supported picture, video and audio for multiple device.",
  author = "tikubonn",
  author_email = "https://twitter.com/tikubonn",
  licence = "MIT",
  install_requires = [],
  dependency_links = [],
  test_suite = "tests",
  packages = find_packages(exclude=["tests"])
)
