
from setuptools import setup, find_packages

with open("README.md", mode="r", encoding="utf-8") as stream:
  long_description = stream.read()

setup(
  name = "moff",
  version = "1.0.0",
  description = "Moff is a markdown dialect that has supported picture, video and audio for multiple device.",
  long_description = long_description,
  licence = "MIT",
  author = "tikubonn",
  author_email = "https://twitter.com/tikubonn",
  url = "https://github.com/tikubonn/moff",
  install_requires = [],
  dependency_links = [],
  test_suite = "tests",
  packages = find_packages(exclude=["tests"]),
  entry_points = {
    "console_scripts": [
      "moff = moff:main",
    ],
  },
  classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "License :: OSI Approved :: MIT License",
  ]
)
