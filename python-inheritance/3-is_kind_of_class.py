#!/usr/binn/python3
"""Defines a instance checker function"""


def is_kind_of_class(obj, a_class):
    """
    Checks if object is an instance of a_class
    or if object is an instance of a_class
    that inherited from.

    Args:
        obj (any): Object to check.
        a_class (class): Class to compare against obj.
    """
    return isinstance(obj, a_class)
