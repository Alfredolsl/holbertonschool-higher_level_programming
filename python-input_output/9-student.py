#!/usr/bin/python3
"""Defines Class Student."""


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

    def to_json(self):
        return self.__dict__
