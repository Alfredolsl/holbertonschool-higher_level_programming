#!/usr/bin/python3
"""Defines a text file reader function"""


def read_file(filename=""):
    """Reads a text file (UTF-8)
    and prints it to stdout."""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
