#!/usr/bin/python3
"""Defines a function."""
import json


def class_to_json(obj):
    """
    Returns the dict description with simple
    data structure for JSON serialization
    of an object.
    """
    return obj.__dict__
