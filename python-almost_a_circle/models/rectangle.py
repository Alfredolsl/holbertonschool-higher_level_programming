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

    @property
    def width(self):
        """Set/Get value of width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets proper value for width.

        Args:
            value (int): Value to set to width.

        Raises:
            TypeError: Width must be integer.
            ValueError: Width must be > 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/Get value of height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets proper value for height.

        Args:
            value (int): Value to set to height.

        Raises:
            TypeError: Height must be integer.
            ValueError: Height must be > 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Sets/Get value of x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets proper value for x.

        Args:
            value (int): Value to set to x.

        Raises:
            TypeError: x must be integer.
            ValueError: x must be > 0.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Sets/Get value of y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets proper value for y.

        Args:
            value (int): Value to set to y.

        Raises:
            TypeError: y must be integer.
            ValueError: y must be > 0.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Sets/Get value of area."""
        return self.__width * self.__height

    def display(self):
        """Displays area of rectangle."""
        for i in range(self.__y):
            print("")

        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            pos = 0
            for arg in args:
                if pos == 0:
                    self.id = arg
                elif pos == 1:
                    self.width = arg
                elif pos == 2:
                    self.height = arg
                elif pos == 3:
                    self.x = arg
                elif pos == 4:
                    self.y = arg
                pos += 1

        elif len(kwargs) != 0:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {"id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y}

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)
