#!/usr/bin/python3
"""Define a Class Square."""


class Square:
    """Represents a square"""


    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the proper value for size"""
        if not isinstance(value, int):
            return TypeError("size must be an integer")
        elif value < 0:
            return ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the current area of the square"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the square with the # character"""
        for i in range(self.__size):
            print("#" * self.__size)
