#!/usr/bin/python3
"""Defines a function that adds a new attribute
to an object if possible."""


def add_attribute(obj, attr, value):
    """Adds a new attribute to object if possible.

    Args:
        obj (any): Object to add an attribute.
        att (str): Name of attribute to add to obj.
        value (any): Value of att.
    Raises:
        TypeError: Can't add new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
