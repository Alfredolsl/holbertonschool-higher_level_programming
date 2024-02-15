#!/usr/bin/python3
"""Defines a is_same_class function."""


def is_same_class(obj, a_class):
    """
    Checks if the obj is exactly an instance
    of the specified class (a_class).
    """
    return isinstance(obj, a_class)
