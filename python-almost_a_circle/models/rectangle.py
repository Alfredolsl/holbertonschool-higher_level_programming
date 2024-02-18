#!/usr/bin/python3
"""Defines a class Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Subclass Rectangle that inherits
    from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance.

        Args:
            width (int): Width of rectangle.
            height (int): Height of rectangle.
            x (int): X position of rectangle.
            y (int): Y position of rectangle.
            id (int): ID of object, derived from Base.

        Raises:
            TypeError: If width, height, x or y is not int.
            ValueError: If width, height, x or y is < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

