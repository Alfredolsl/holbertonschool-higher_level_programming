#!/usr/bin/python3
"""Defines a Rectangle class."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle."""
    def __init__(self, width, height):
        """Initializes Rectangle.

        Args:
            width (int): Width of rectangle.
            height (int): Height of rectangle.
        """
        super().__init__
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns calculated area of a rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() function and
        str() representation of a Triangle."""
        return "[{}] {}/{}".format(self.__class__.__name__, self.__width, self.__height)
