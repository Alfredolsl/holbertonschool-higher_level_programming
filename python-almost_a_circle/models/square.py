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

    def update(self, *args, **kwargs):
        if len(args) != 0:
            pos = 0
            for arg in args:
                if pos == 0:
                    self.id = arg
                elif pos == 1:
                    self.size = arg
                elif pos == 2:
                    self.x = arg
                elif pos == 3:
                    self.y = arg
                pos += 1
        elif len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        return {"id": self.id, "x": self.x, "size": self.size,
                "y": self.y}