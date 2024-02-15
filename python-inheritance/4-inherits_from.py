#!/usr/bin/python3
"""Defines a object inhertiance checker function"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class
    that inherited (directly or indirectly) from
    the specified class.

    Args:
        obj (any): Object to check.
        a_class (class): Class to compare instance of obj.

    Returns:
        True if the object is an instance
        that is inherited (directly or indirectly)
        from the specified class;
        otherwise False."""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
