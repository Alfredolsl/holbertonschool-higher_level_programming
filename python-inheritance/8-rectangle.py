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
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
