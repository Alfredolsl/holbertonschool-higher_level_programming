#!/usr/bin/python3
"""Defines a append-write file function."""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a
    UTF-8 file.

    Args:
        filename (str): Filename to append text.
        text (str): Text to append to file.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
