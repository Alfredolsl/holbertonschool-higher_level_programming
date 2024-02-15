#!/usr/bin/python3
"""Defines a MyList class."""


class MyList(list):
    """A subclass of list."""
    def __init__(self):
        """Initializes MyList."""
        super().__init__()

    def print_sorted(self):
        """Prints a sorted list."""
        print(sorted(self))
