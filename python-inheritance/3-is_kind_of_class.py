#!/usr/bin/python3
"""Defines a instance checker function"""


def is_kind_of_class(obj, a_class):
    """
    Checks if object is an instance of a_class
    or if object is an instance of a_class
    that inherited from.

    Args:
        obj (any): Object to check.
        a_class (class): Class to compare against obj.
    Returns:
        If obj is an instance or inherited instance
        of a_class True, otherwise, False
    """
    if isinstance(obj, a_class):
        return True

    return False
