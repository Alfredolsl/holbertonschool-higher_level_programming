#!/usr/bin/python3
"""Defines a file writer function."""


def write_file(filename="", text=""):
    """
    Writes a string to a UTF-8 file.

    Args:
        filename (str): Name/Path of the file.
        text (str): Text to write on file.

    Returns: Number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
