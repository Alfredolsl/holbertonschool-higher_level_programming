#!/usr/bin/python3
"""Defines a is_same_class function."""


def is_same_class(obj, a_class):
    """
    Checks if the obj is EXACTLY an instance
    of the specified class (a_class).

    Args:
        obj (any): Object to check.
        a_class (class): The class to match the type of obj.

    Returns:
        True if obj matches the type of a_class,
        otherwise False
    """
    if type(obj) is a_class:
        return True
    return False
