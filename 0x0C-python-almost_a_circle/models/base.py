#!/usr/bin/python3
""" Base module
Houses a Base class with private attributes
"""
import json
import csv
import os.path


class Base:
    """ Defines the class Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes an instance of class

        Args:
            id: (int) Defauls as None

        """

        if id is not None:
            self.id = id
        else:
            BAse.__nb_objects += 1
            self.id = BAse.__nb_objects
