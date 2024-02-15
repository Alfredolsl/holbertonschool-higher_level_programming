#!/usr/bin/python3
"""Defines a JSON representationfunction."""
import json


def to_json_string(my_obj):
    """Returns a obj into JSON representation."""
    return json.dumps(my_obj)
