#!/usr/bin/python3
"""Defines a Square class that inherits from Rectanlge."""
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
