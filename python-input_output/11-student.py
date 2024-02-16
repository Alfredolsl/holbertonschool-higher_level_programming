#!/usr/bin/python3
"""Defines a class Student."""


class Student():
    """Represents a student."""
    def __init__(self, first_name, last_name, age):
        """
        Initializes Student instance.

        Args:
            first_name (str): First name of student.
            last_name (str): Last name of student.
            age (str): Age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list and all([type(i) is str for i in attrs]):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        for i, j in json.items():
            setattr(self, i, j)
