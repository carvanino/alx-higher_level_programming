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

        Args:
            list_objs: a list of class instances
        """

        filename = '{}.json'.format(cls.__name__)
        print(filename)
        list_dict = []  # a list of object dictionaries
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

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of JSON string representation from json_string
        """

        if json_string is None or len(json_string) == 0:
            return {}
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attribute set

        Args:
            **dictionary: used as a keyword argument **kwargs

        Return:
            The instance created

        """

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 3, 2, 0, 1)  # (width, height, x, y, id)
        elif cls.__name__ == 'Square':
            dummy = cls(4, 2, 2, 1)  # (size, x, y, id)
        dummy.update(**dictionary)
        return dummy  # The instance that has all attributes set

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances
        """

        filename = '{}.json'.format(cls.__name__)
        if filename is None:
            return []
        list_instance = []
        with open(filename, 'r') as f:
            json_string = f.read()
        list_dict = cls.from_json_string(json_string)

        for i in range(len(list_dict)):
            list_instance.append(cls.create(**list_dict[i]))

        return list_instance
