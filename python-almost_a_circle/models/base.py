#!/usr/bin/python3
"""Defines a base model Base."""


class Base:
    """Represents Base Model
    As the name suggests, this class
    will be the base class of all other
    classes in this project.

    Private Class Attributes:
        __nb_objects (int): Number of Base objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes Base.

        Args:
            id (int): id of object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
