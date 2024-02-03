#!/usr/bin/python3
"""define a class Square"""


class Square:
    """represents a square"""

    def __init__(self, size=0):
        """initialize a new Square.

        Args:
            size (int): the size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """__size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """__size setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns total area of the square"""
        return self.__size * self.__size
