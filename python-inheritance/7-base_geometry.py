#!/usr/bin/python3
"""Defines a BaseGeometry module."""


class BaseGeometry:
    """Represents BaseGeometry."""
    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as integer.

        Args:
            name (string): Name of parameter.
            value (int): Value to validate.

        Raises:
            TypeError: Value is not an integer.
            ValueError: Value is less or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
