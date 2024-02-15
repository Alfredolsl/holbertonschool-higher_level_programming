#!/usr/bin/python3
"""Defines a JSON to Object function."""
import json


def from_json_string(my_str):
    """Returns Python object representation of
    JSON string."""
    return json.loads(my_str)
