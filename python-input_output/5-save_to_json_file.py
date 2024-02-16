#!/usr/bin/python3
"""Defines a object writer to text file function."""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a txt file,
    using a JSON representation.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
