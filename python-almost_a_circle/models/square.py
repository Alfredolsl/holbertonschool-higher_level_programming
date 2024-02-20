#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square instance.

        Args:
            size (int): Size of square.
            x (int): X position of square.
            y (int): Y position of square.
            id (int): Identity number of new square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.height)
