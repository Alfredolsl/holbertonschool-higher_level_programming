#!/usr/bin/python3
"""Defines a class rectangle."""


class Rectangle:
    """Represents a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            print_symbol (any): The symbol to represent the rectangle size.
        """
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * self.__width

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """Returns the size of the rectangle with '#' characters"""
        if self.__height == 0 or self.__width == 0:
            return ""

        rect = []
        for n in range(self.__height):
            [rect.append(str(self.print_symbol)) for n in range(self.__width)]
            if n != self.__height - 1:
                rect.append("\n")

        return "".join(rect)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect1, rect2):
        """Returns the biggest rectangle
        based on the area.

        Args:
            rect1 (int): Rectangle 1
            rect2 (int): Rectangle 2
        """
        if rect1.__class__.__name__ != "Rectangle":
            raise TypeError("rect_1 must be a rectangle")
        elif rect2.__class__.__name__ != "Rectangle":
            raise TypeError("rect_2 must be a rectangle")

        if rect1.area() >= rect2.area():
            return rect1
        else:
            return rect2
