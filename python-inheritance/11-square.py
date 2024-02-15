#!/usr/bin/python3
"""Defines a Square subclass that inherits
from Rectangle parent class."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Represents a square."""
    def __init__(self, size):
        """Initializes a Square.

        Args:
            size (int): Square size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns when called str() or print()
        representation of a Square."""
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__size, self.__size)
