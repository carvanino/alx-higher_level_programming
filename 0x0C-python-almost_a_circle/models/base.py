#!usr/bin/python3
"""Base Module
Houses a Base class with private attributes
"""
import json


class Base:
    """ Defines the class Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes an Instance of class

        Args:
            id: (int) Defaults as None

        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of
        list_dictinaries
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
