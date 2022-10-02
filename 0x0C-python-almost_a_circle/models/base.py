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
        if id is not None:
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

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs
        to a file
        """

        filename = '{}.json'.format(cls.__name__)
        print(filename)
        list_dict = []
        if list_objs is None:
            with open(filename, mode='w') as f:
                f.write(list_dict)
        else:
            for i, obj in enumerate(list_objs):
                print(i)
                list_dict.append(obj.to_dictionary())
            json_string = cls.to_json_string(list_dict)
            with open(filename, mode='w') as f:
                f.write(json_string)
