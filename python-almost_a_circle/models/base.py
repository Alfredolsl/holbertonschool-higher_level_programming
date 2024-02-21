#!/usr/bin/python3
"""Defines a base model Base."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json" 
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dict_objects = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(dict_objects))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary != {}:
            if cls.__name__ == "Square":
                dummy_instance = cls(1)
            else:
                dummy_instance = cls(1, 1)

            dummy_instance.update(**dictionary)
            return dummy_instance

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                dict_objects = Base.from_json_string(f.read())
                return [cls.create(**d) for d in dict_objects]
        except IOError:
            return []
