#!/usr/bin/python3
"""Defines a function that prints a square with the character '#'."""


def print_square(size):
    """Prints a square with the character '#'

    Raises:
    TypeError: Size must be an integer.
    ValueError: Size must be >= 0.
    TypeError: If size is a float and is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif size:
        raise TypeError("size must be an integer")

    for i in range(0, size):
        print("#" * size)
