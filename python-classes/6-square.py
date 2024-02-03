#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square
        
        Args:
            size(int): size of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """retrieves private attribute size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets correctly size value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """retrieves private attribute position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets correctly position value"""
        if len(value) != 2 or not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        
        if not all(isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        
        self.__position = value

    def area(self):
        """returns current square area"""
        return self.__size * self.__size

    def my_print(self):
        "prints in stdout the square with the character #"
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]

        for i in range(0, self.__size):
            print(" " * self.position[0], end="")
            print("#" * self.__size, end="")
            print("")
