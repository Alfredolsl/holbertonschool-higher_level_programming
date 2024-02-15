#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """MyInt has == and != operators inverted."""

    def __eq__(self, value):
        """Overrides __eq__ method.
        __eq__ is equal with object.
        Replaces == operator with !=."""
        return self.real != value

    def __ne__(self, value):
        """Overrides __ne__ method.
        __ne__ is not equal with object.
        Replaces != operator with ==."""
        return self.real == value
